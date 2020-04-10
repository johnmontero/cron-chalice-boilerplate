import json
from chalice import Chalice, Response    
from .exceptions import ErrorHTTPStatusCode

_CONTENT_TYPE_JSON = "application/json"
_HTTP_STATUS_CODE_OK = 200

def validate_response_metadata(response):
    http_status_code = response['ResponseMetadata']['HTTPStatusCode']
    if not http_status_code == _HTTP_STATUS_CODE_OK:
        raise ErrorHTTPStatusCode('Error HTTPStatusCode: {}'.format(http_status_code))