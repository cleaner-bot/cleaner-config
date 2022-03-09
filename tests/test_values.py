import pytest
from cleaner_conf.exceptions import ValidationError
from cleaner_conf.values import (
    IntegerValue,
    BooleanValue,
    SnowflakeValue,
    URLValue,
    BotTokenValue,
    ListValue,
)


def test_integer_value():
    value = IntegerValue(default=0, description=None, hidden=True)
    assert value.default == 0
    assert value.min is None
    assert value.max is None
    assert value.hidden is True

    value.validate_string("0")
    value.validate_string("123")


def test_integer_range():
    value = IntegerValue(default=10, min=5, max=20, description=None)

    with pytest.raises(ValidationError):
        value.validate_string("2")
    with pytest.raises(ValidationError):
        value.validate_string("25")

    value.validate_string("5")
    value.validate_string("20")


def test_boolean():
    value = BooleanValue(default=True, description=None)

    value.validate_string("yes")
    value.validate_string("no")

    assert value.from_string("yes") is True
    assert value.to_string(True) == "yes"
    assert value.from_string("no") is False
    assert value.to_string(False) == "no"


def test_snowflake():
    value = SnowflakeValue(default=0, description=None)

    assert value.max == value.SNOWFLAKE_MAX

    value.validate_string(str(value.SNOWFLAKE_MAX))

    with pytest.raises(ValidationError):
        value.validate_string(str(value.SNOWFLAKE_MAX + 1))


def test_url():
    value = URLValue(description=None)

    value.validate_string("")
    value.validate_string("http://example.com")


def test_bottoken():
    value = BotTokenValue()

    value.validate_string("")
    with pytest.raises(ValidationError):
        value.validate_string("test")


def test_list():
    value = ListValue(
        item=BooleanValue(default=True, description=None), description=None
    )

    value.validate_string("")
    value.validate_string("yes")
    value.validate_string("yes,yes,yes,no,no,yes")

    assert value.from_string("yes,yes,yes,no,no,yes") == [
        True,
        True,
        True,
        False,
        False,
        True,
    ]
    assert (
        value.to_string([True, True, True, False, False, True])
        == "yes,yes,yes,no,no,yes"
    )
