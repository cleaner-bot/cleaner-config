import pytest
from cleaner_conf.exceptions import ValidationError
from cleaner_conf.helper import (
    try_int,
    try_boolean,
    assert_range,
    try_valid_url,
    try_valid_bottoken,
)


def test_try_int():
    with pytest.raises(ValidationError):
        try_int("9" * 101)

    try_int("9" * 101, maxlen=200)

    with pytest.raises(ValidationError):
        try_int("abcdef")

    assert try_int("123") == 123


def test_try_boolean():
    with pytest.raises(ValidationError):
        try_boolean(True)

    with pytest.raises(ValidationError):
        try_boolean("test")

    assert try_boolean("yes") is True
    assert try_boolean("no") is False


def test_assert_range():
    assert_range(0)

    with pytest.raises(ValidationError):
        assert_range(0, min=1)

    with pytest.raises(ValidationError):
        assert_range(10, max=5)


def test_try_valid_url():
    with pytest.raises(ValidationError, match="url does not have a scheme"):
        try_valid_url("test.com")

    with pytest.raises(ValidationError, match="url scheme is not allowed"):
        try_valid_url("ftp://test.com")

    with pytest.raises(ValidationError, match="url does not have a hostname"):
        try_valid_url("http:///")

    with pytest.raises(
        ValidationError, match="urls with username or password are not allowed"
    ):
        try_valid_url("http://user@test.com")
    with pytest.raises(
        ValidationError, match="urls with username or password are not allowed"
    ):
        try_valid_url("http://:pass@test.com")
    with pytest.raises(
        ValidationError, match="urls with username or password are not allowed"
    ):
        try_valid_url("http://user:pass@test.com")

    with pytest.raises(ValidationError, match="url has invalid port"):
        try_valid_url("http://test.com:xd")

    with pytest.raises(ValidationError, match="url port is not allowed"):
        try_valid_url("http://test.com:20")

    try_valid_url("http://test.com:80/some_path")


def test_try_valid_bottoken():
    with pytest.raises(ValidationError):
        try_valid_bottoken("")
    with pytest.raises(ValidationError):
        try_valid_bottoken(".")
    with pytest.raises(ValidationError):
        try_valid_bottoken("...")

    with pytest.raises(ValidationError):
        try_valid_bottoken("..")
    with pytest.raises(ValidationError):
        try_valid_bottoken("YQ==..")
    with pytest.raises(ValidationError):
        try_valid_bottoken("YQ..")

    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==..")
    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==.aaa..")
    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==.aaaaaaa.")
    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==.123456.")

    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==.aaaaaa.")
    with pytest.raises(ValidationError):
        try_valid_bottoken("MQ==.aaaaaa.___________________________")

    try_valid_bottoken("MQ==.aaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaa")
