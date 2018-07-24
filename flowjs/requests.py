import os
from tempfile import NamedTemporaryFile

from .interfaces import IRequest, IFile


class CycloneRequest(IRequest):

    def __init__(self, request):
        self._request = request

        self._file = None
        if len(self._request.files) != 0:
            self._file = File(self._request.files['file'][0])

    def _get_param(self, key):
        if key not in self._request.arguments:
            return None
        if len(self._request.arguments[key]) == 0:
            return None
        return self._request.arguments[key][0]

    def get_file_name(self):
        return self._get_param('flowFilename')

    def get_total_size(self):
        return int(self._get_param('flowTotalSize'))

    def get_identifier(self):
        return self._get_param('flowIdentifier')

    def get_relative_path(self):
        return self._get_param('flowRelativePath')

    def get_total_chunks(self):
        return int(self._get_param('flowTotalChunks'))

    def get_default_chunk_size(self):
        return int(self._get_param('flowChunkSize'))

    def get_current_chunk_number(self):
        return int(self._get_param('flowChunkNumber'))

    def get_current_chunk_size(self):
        return int(self._get_param('flowCurrentChunkSize'))

    def is_fusty_flow_request(self):
        return False

    def get_file(self):
        return self._file

    def is_post(self):
        return self._request.method == "POST"

    def is_get(self):
        return self._request.method == "GET"


class File(IFile):

    def __init__(self, file_):
        self._content_type = file_['content_type']
        self._name = file_['filename']
        self._error = None
        with NamedTemporaryFile(delete=False) as f:
            f.write(file_['body'])
            self._tmp_name = f.name
            self._size = os.path.getsize(f.name)

    def get_tmp_name(self):
        return self._tmp_name

    def get_size(self):
        return self._size

    def get_error(self):
        return self._error

    def get_name(self):
        return self._name

    def get_type(self):
        return self._content_type
