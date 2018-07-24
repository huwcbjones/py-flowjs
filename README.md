flow.js python server
=======================

Python library for handling chunk uploads (based on flow-php-server). Library contains helper methods for:
 * Testing if uploaded file chunk exists.
 * Validating file chunk
 * Creating separate chunks folder
 * Validating uploaded chunks
 * Merging all chunks to a single file

The library currently only supports Cyclone, but it is trivial to implement interfaces for other web servers (flask, etc).

This library is compatible with HTML5 file upload library: https://github.com/flowjs/flow.js

How to get started?
--------------
Install the pip module:
```
pip install flowjs
```

Create a new py file named `upload.py`:
```python
# Import flowjs
import uuid
import os

import flowjs

config = flowjs.Config()
request = flowjs.requests.CycloneRequest(cyclone_http_request)
upload_directory = "/path/to/final/upload/directory"
upload_file_name = uuid.uuid1().hex + "_" + request.get_file_name()
upload_path = os.path.join(upload_directory, upload_file_name)
try:
    result = flowjs.save(upload_path, config, request)
    if result:
        # file was saved to path
        pass
    else:
        # not final chunk or invalid request
        pass
except flowjs.NoContent:
    # Set status to 204 No Content
    # Do _not_ return any content in the response body
except flowjs.BadRequest:
    # Set status to 400 Bad Request
```

Config
------

## tempDir
Temporary directory where chunks are stored (will default to your system temp dir).

Make sure that the temp path exists and is writable. All chunks will be saved in this folder.


## hashNameCallback
Function applied to the request to generate a unique identifier for the file.

Defaults to a SHA1 hash of the `flowIdentifier`


## preProcessCallback
Function applied before each chunk is merged into the resultant file.


## deleteChunksOnSave
Should the server delete the file chunks after it saves the final file.

Defaults to `True`


Other Web Servers
-----------------

To use this module with other webservers, implement the `IRequest` and `IFile` interfaces with your webserver's specific implementation details.

Contribution
------------

Your participation in development is very welcome!
