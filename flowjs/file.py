import logging
import os

from filelock import FileLock

from flowjs.interfaces import IRequest, IConfig, IFile


class ChunkedFile:

    def __init__(self, config, request):
        # type: (IConfig, IRequest) -> None

        if config is None:
            raise TypeError('Argument passed to config cannot be None!')
        self._config = config  # type: IConfig

        if request is None:
            raise TypeError('Argument passed to request cannot be None!')
        self._request = request  # type: IRequest

        hash_name_callback = self._config.get_hash_name_callback()
        self._identifier = hash_name_callback(request)

    def get_identifier(self):
        # type: () -> str
        """
        Get file identifier
        :return:
        """
        return self._identifier

    def get_chunk_path(self, index):
        # type: (int) -> str
        """
        Return chunk path
        :param index:
        :return:
        """
        return os.path.join(self._config.get_temp_dir(), self._identifier + "_" + str(index))

    def check_chunk(self):
        # type: () -> bool
        """
        Check if chunk exist
        :return:
        """
        index = self._request.get_current_chunk_number()
        path = self.get_chunk_path(index)
        if not os.path.exists(path):
            logging.debug("check_chunk: Warning, path does not exist, path: {}".format(path))
            return False
        logging.debug("check_chunk: Chunk exists at {}".format(path))
        return True

    def validate_chunk(self):
        # type: () -> bool
        file_ = self._request.get_file()  # type: IFile
        logging.debug("validate_chunk: temp_name: {}/file_size: {}".format(file_.get_tmp_name(), file_.get_size()))
        if file_ is None:
            logging.debug("validate_chunk: Warning, File is None")
            return False
        if file_.get_tmp_name() is None or file_.get_size() is None or file_.get_error() is not None:
            logging.debug(
                "validate_chunk: error: {}".format(file_.get_error()))
            return False
        if self._request.get_current_chunk_size() != file_.get_size():
            logging.debug("validate_chunk: Warning, chunk size matches file_ size")
            # return False
        logging.debug("validate_chunk: Chunk was successfully validated!")
        return True

    def save_chunk(self):
        # type: () -> bool
        file_ = self._request.get_file()
        chunk_path = self.get_chunk_path(self._request.get_current_chunk_number())
        os.rename(file_.get_tmp_name(), chunk_path)
        logging.debug("save_chunk: Chunk was saved to {}".format(chunk_path))
        return True

    def validate_file(self):
        # type: () -> bool
        """
        Check if file upload is complete
        :return:
        """
        total_chunks = self._request.get_total_chunks()
        total_chunks_size = 0
        for i in range(1, total_chunks + 1):
            file_ = self.get_chunk_path(i)
            if not os.path.exists(file_):
                logging.debug("validate_file: Warning, missing chunk at {}".format(file_))
                return False
            chunk_size = os.path.getsize(file_)
            total_chunks_size = total_chunks_size + chunk_size
            logging.debug("validate_file: chunk {}, {}/{} (chunk/total)".format(i, chunk_size, total_chunks_size))
        if self._request.get_total_size() != total_chunks_size:
            logging.debug("validate_file: Warning, file size does not match uploaded chunks size ({} != {})".format(
                self._request.get_total_size(), total_chunks_size))
            return False
        logging.debug("validate_file: Chunks successfully validated!")
        return True

    def save(self, destination, timeout=5):
        # type: (str, int) -> bool
        """
        Merge all chunks to single file
        :param timeout: Timeout to acquire lock
        :raises IOError
        :param destination:
        :return:
        """
        with FileLock(destination + ".lock", timeout):
            with open(destination, "wb") as fh:
                total_chunks = self._request.get_total_chunks()

                pre_process_chunk = self._config.get_preprocess_callback()
                for i in range(1, total_chunks + 1):
                    file_ = self.get_chunk_path(i)
                    with open(file_, "rb") as chunk:
                        if pre_process_chunk is not None:
                            pre_process_chunk(chunk)
                        fh.write(chunk.read())
            if self._config.get_delete_chunks_on_save():
                self.delete_chunks()
            logging.debug("save: Chunks combined into {}".format(destination))
        return True

    def delete_chunks(self):
        # type: () -> None
        """
        Delete chunks dir
        :return:
        """
        total_chunks = self._request.get_total_chunks()
        [os.remove(self.get_chunk_path(i)) for i in range(1, total_chunks + 1)]
