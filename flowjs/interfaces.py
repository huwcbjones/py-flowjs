import abc


class IRequest(object):
    __metaclass__ = abc.ABCMeta

    def is_post(self):
        # type: (None) -> bool
        """
        Returns true if the HTTP method was POST
        :return:
        """
        pass

    def is_get(self):
        # type: (None) -> bool
        """
        Returns true if the HTTP method was GET
        :return:
        """
        pass

    def get_file_name(self):
        # type: (None) -> str
        """
        Get uploaded file name
        :return:
        """
        pass

    def get_total_size(self):
        # type: (None) -> int
        """
        Get total file size in bytes
        :return:
        """
        pass

    def get_identifier(self):
        # type: (None) -> str
        """
        Get file unique identifier
        :return:
        """
        pass

    def get_relative_path(self):
        # type: (None) -> str
        """
        Get file relative path
        :return:
        """
        pass

    def get_total_chunks(self):
        # type: (None) -> int
        """
        Get total chunks number
        :return:
        """
        pass

    def get_default_chunk_size(self):
        # type: (None) -> int
        """
        Get default chunk size
        :return:
        """
        pass

    def get_current_chunk_number(self):
        # type: (None) -> int
        """
        Get current uploaded chunk number, starts with 1
        :return:
        """
        pass

    def get_current_chunk_size(self):
        # type: (None) -> int
        """
        Get current uploaded chunk size
        :return:
        """
        pass

    def is_fusty_flow_request(self):
        # type: (None) -> bool
        """
        Checks if request is formed by fusty flow
        :return:
        """
        pass

    def get_file(self):
        # type: (None) -> IFile or None
        """
        Return files
        :return:
        """
        pass


class IConfig(object):
    __metaclass__ = abc.ABCMeta

    def set_temp_dir(self, path):
        # type: (str) -> None
        """
        Set path to temporary directory for chunks storage
        :param path:
        :return:
        """
        pass

    def get_temp_dir(self):
        # type: (None) -> str
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
        # type: (None) -> callable
        """
        Generate chunk identifier
        :rtype: function
        :return:
        """
        pass

    def set_preprocess_callback(self, callback):
        """
        Callback to pre-process chunk
        :param callback:
        :return:
        """
        # type: callable -> None
        pass

    def get_preprocess_callback(self):
        """
        Callback to pre-process chunk
        :return:
        """
        # type: None -> callable
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
        # type: (None) -> bool
        """
        Delete chunks on save
        :return:
        """
        pass


class IFile(object):
    __metaclass__ = abc.ABCMeta

    def get_tmp_name(self):
        # type: (None) -> str
        """
        Return temporary file name
        :return:
        """
        pass

    def get_size(self):
        # type: (None) -> int
        """
        Return file size in bytes
        :return:
        """
        pass

    def get_error(self):
        # type: (None) -> str

        pass

    def get_name(self):
        # type: (None) -> str
        """
        Return the name of the file (provided by the client, be wary)
        :return:
        """
        pass

    def get_type(self):
        # type: (None) -> str
        """
        Return the MIME type of the file (provided by the client, be wary)
        :return:
        """
        pass







