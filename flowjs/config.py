from hashlib import sha1
from tempfile import gettempdir

from .interfaces import IConfig
from .interfaces import IRequest


class Config(IConfig):
    def __init__(self, config=None):
        # type: (dict) -> None
        if config is None:
            self._config = {}
        else:
            self._config = config

    def _get_config(self, key):
        if key in self._config:
            return self._config[key]
        return None

    def set_temp_dir(self, path):
        # type: (str) -> None
        """
        Set path to temporary directory for chunks storage
        :param path:
        :return:
        """
        self._config['tempDir'] = path

    def get_temp_dir(self):
        # type: (None) -> str
        """
        Get path to temporary directory for chunks storage
        :return:
        """
        return self._get_config('tempDir') or gettempdir()

    def set_hash_name_callback(self, callback):
        # type: (callable) -> None
        """
        Set chunk identifier
        :param callback:
        :return:
        """
        self._config['hashNameCallback'] = callback

    def get_hash_name_callback(self):
        # type: (None) -> callable
        """
        Generate chunk identifier
        :rtype: function
        :return:
        """
        return self._get_config('hashNameCallback') or hash_name_callback

    def set_preprocess_callback(self, callback):
        """
        Callback to pre-process chunk
        :param callback:
        :return:
        """
        # type: callable -> None
        self._config['preprocessCallback'] = callback

    def get_preprocess_callback(self):
        """
        Callback to pre-process chunk
        :return:
        """
        # type: None -> callable
        return self._get_config('preprocessCallback') or None

    def set_delete_chunks_on_save(self, delete):
        # type: (bool) -> None
        """
        Delete chunks on save
        :param delete:
        :return:
        """
        self._config['deleteChunksOnSave'] = delete

    def get_delete_chunks_on_save(self):
        # type: (None) -> bool
        """
        Delete chunks on save

        :return:
        """
        return self._get_config('deleteChunksOnSave') or True


def hash_name_callback(request):
    # type: (IRequest) -> str
    """
    Generate chunk identifier
    :param request:
    :return:
    """
    s = sha1()
    s.update(request.get_identifier())
    return s.hexdigest()
