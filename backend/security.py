from flask import request
from functools import wraps
from .config import settings
from .errors import ApiError

def require_api_key(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not settings.API_KEY: # no key in dev
            return fn(*args, **kwargs)
        key = request.headers.get('X-API-KEY')
        if key != settings.API_KEY:
            raise ApiError("Invalid API key", status_code=401, code="unauthorized")
        return fn(*args, **kwargs)
    return wrapper