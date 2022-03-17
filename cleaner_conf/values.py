import typing

from .helper import (
    try_boolean,
    try_int,
    assert_range,
    try_valid_url,
    try_valid_bottoken,
)


class BaseValue:
    default: typing.Any
    description: str | None = None
    hidden: bool = False

    def __init__(
        self,
        *,
        default: typing.Any,
        description: str | None = None,
        hidden: bool = False
    ) -> None:
        self.default = default
        self.description = description
        self.hidden = hidden

    def validate_string(self, value: str):
        pass  # pragma: no cover

    def to_string(self, value: typing.Any) -> str:
        return str(value)

    def from_string(self, value: str) -> typing.Any:
        return value


class IntegerValue(BaseValue):
    default: int

    def __init__(self, *, min: int = None, max: int = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.min = min
        self.max = max

    def validate_string(self, value: str):
        value_as_int = try_int(value)
        assert_range(value_as_int, self.min, self.max)

    def from_string(self, value: str) -> typing.Any:
        return try_int(value)


class BooleanValue(BaseValue):
    default: bool

    def validate_string(self, value: str):
        try_boolean(value)

    def from_string(self, value: str) -> bool:
        return try_boolean(value)

    def to_string(self, value: bool) -> str:
        return "yes" if value else "no"


class URLValue(BaseValue):
    default: str

    def __init__(self, **kwargs) -> None:
        kwargs.setdefault("default", "")
        super().__init__(**kwargs)

    def validate_string(self, value: str):
        if value:
            try_valid_url(value)


class BotTokenValue(BaseValue):
    default: str

    def __init__(self, **kwargs) -> None:
        kwargs.setdefault("default", "")
        super().__init__(**kwargs)

    def validate_string(self, value: str):
        if value:
            try_valid_bottoken(value)


class ListValue(BaseValue):
    default: list

    def __init__(self, *, item: BaseValue, **kwargs) -> None:
        kwargs.setdefault("default", [])
        super().__init__(**kwargs)
        self.item = item

    def validate_string(self, value: str):
        if value:
            for text in value.split(","):
                self.item.validate_string(text)

    def from_string(self, value: str) -> list[typing.Any]:
        if not value:
            return []
        return [self.item.from_string(x) for x in value.split(",")]

    def to_string(self, value: list[typing.Any]) -> str:
        if not value:
            return ""
        return ",".join(self.item.to_string(x) for x in value)


class SnowflakeValue(IntegerValue):
    SNOWFLAKE_MAX = 1 << 63

    def __init__(self, **kwargs) -> None:
        super().__init__(min=0, max=self.SNOWFLAKE_MAX, **kwargs)


class PlanValue(IntegerValue):
    def __init__(self, **kwargs) -> None:
        super().__init__(min=0, max=3, **kwargs)


DictType = dict[str, BaseValue]
