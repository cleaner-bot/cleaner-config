import base64
import binascii
from urllib.parse import urlparse

from .exceptions import ValidationError


def try_int(value: str, maxlen: int = 100) -> int:
    if len(value) > maxlen:
        raise ValidationError("value is too long")
    if not value.isdigit():
        raise ValidationError("value is not an integer")
    return int(value)


def try_boolean(value: str) -> bool:
    if value == "yes":
        return True
    elif value == "no":
        return False
    raise ValidationError("value is not 'yes' or 'no'")


def assert_range(value: float, min: float = None, max: float = None):
    """[min, max]"""
    if max is not None and value > max:
        raise ValidationError(f"value is higher than the max allowed ({max})")
    if min is not None and value < min:
        raise ValidationError(f"value is lower than the min allowed ({min})")


def try_valid_url(value: str):
    url = urlparse(value)

    if not url.scheme:
        raise ValidationError("url does not have a scheme")
    if url.scheme not in ("http", "https"):
        raise ValidationError("url scheme is not allowed")
    if not url.netloc:
        raise ValidationError("url does not have a hostname")
    if url.username or url.password:
        raise ValidationError("urls with username or password are not allowed")

    try:
        port = url.port
    except ValueError:
        raise ValidationError("url has invalid port")

    if port is not None and port not in (80, 443):
        raise ValidationError("url port is not allowed")

    return url


def try_valid_bottoken(value: str):
    if value.count(".") != 2:
        raise ValidationError("invalid bot token")

    client_id, timestamp, nonce = value.split(".")
    try:
        try_int(base64.b64decode(client_id).decode())
    except binascii.Error:
        raise ValidationError("invalid bot token")
    if not 6 >= len(timestamp) >= 5 or not timestamp.isalpha():
        raise ValidationError("invalid bot token")

    if len(nonce) != 27 or not nonce.replace("-", "").isalnum():
        raise ValidationError("invalid bot token")

    return client_id
