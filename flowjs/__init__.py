from flowjs.file import ChunkedFile
from flowjs.interfaces import IConfig, IRequest
from flowjs.config import Config

name = "flowjs"


class BadRequest(BaseException):
    pass


class NoContent(BaseException):
    pass


def save(destination, config_, request):
    # type: (str, IConfig, IRequest) -> bool
    if not isinstance(config_, IConfig):
        raise TypeError('Object passed to config was not of type `IConfig`')

    file_ = ChunkedFile(config_, request)
    if request.is_get():
        if file_.check_chunk():
            return True
        else:
            raise NoContent()
    else:
        if file_.validate_chunk():
            file_.save_chunk()
        else:
            raise BadRequest()

    if file_.validate_file() and file_.save(destination):
        return True
    return False
