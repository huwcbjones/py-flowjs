import abc


class IRequest(abc.ABC):

    def is_post(self):
        # type: () -> bool
        """
        Returns true if the HTTP method was POST
        :return:
        """
        pass

    def is_get(self):
        # type: () -> bool
        """
        Returns true if the HTTP method was GET
        :return:
        """
        pass

    def get_file_name(self):
        # type: () -> str
        """
        Get uploaded file name
        :return:
        """
        pass

    def get_total_size(self):
        # type: () -> int
        """
        Get total file size in bytes
        :return:
        """
        pass

    def get_identifier(self):
        # type: () -> str
        """
        Get file unique identifier
        :return:
        """
        pass

    def get_relative_path(self):
        # type: () -> str
        """
        Get file relative path
        :return:
        """
        pass

    def get_total_chunks(self):
        # type: () -> int
        """
        Get total chunks number
        :return:
        """
        pass

    def get_default_chunk_size(self):
        # type: () -> int
        """
        Get default chunk size
        :return:
        """
        pass

    def get_current_chunk_number(self):
        # type: () -> int
        """
        Get current uploaded chunk number, starts with 1
        :return:
        """
        pass

    def get_current_chunk_size(self):
        # type: () -> int
        """
        Get current uploaded chunk size
        :return:
        """
        pass

    def is_fusty_flow_request(self):
        # type: () -> bool
        """
        Checks if request is formed by fusty flow
        :return:
        """
        pass

    def get_file(self):
        # type: () -> IFile or None
        """
        Return files
        :return:
        """
        pass


class IConfig(abc.ABC):

    def set_temp_dir(self, path):
        # type: (str) -> None
        """
        Set path to temporary directory for chunks storage
        :param path:
        :return:
        """
        pass

    def get_temp_dir(self):
        # type: () -> str
        """
        Get path to temporary directory for chunks storage
        :return:
        """
        pass

    def set_hash_name_callback(self, callback):
        # type: (callable) -> None
        """
        Set chunk identifier
        :param callback:
        :return:
        """
        pass

    def get_hash_name_callback(self):
        # type: () -> callable
        """
        Generate chunk identifier
        :rtype: function
        :return:
        """
        pass

    def set_preprocess_callback(self, callback):
        # type: (callable) -> None
        """
        Callback to pre-process chunk
        :param callback:
        :return:
        """
        pass

    def get_preprocess_callback(self):
        # type: () -> callable
        """
        Callback to pre-process chunk
        :return:
        """
        pass

    def set_delete_chunks_on_save(self, delete):
        # type: (bool) -> None
        """
        Delete chunks on save
        :param delete:
        :return:
        """
        pass

    def get_delete_chunks_on_save(self):
        # type: () -> bool
        """
        Delete chunks on save
        :return:
        """
        pass


class IFile(abc.ABC):

    def get_tmp_name(self):
        # type: () -> str
        """
        Return temporary file name
        :return:
        """
        pass

    def get_size(self):
        # type: () -> int
        """
        Return file size in bytes
        :return:
        """
        pass

    def get_error(self):
        # type: () -> str

        pass

    def get_name(self):
        # type: () -> str
        """
        Return the name of the file (provided by the client, be wary)
        :return:
        """
        pass

    def get_type(self):
        # type: () -> str
        """
        Return the MIME type of the file (provided by the client, be wary)
        :return:
        """
        pass
