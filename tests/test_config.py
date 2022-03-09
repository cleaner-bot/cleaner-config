from cleaner_conf import config, Config


def test_typehint():
    keys_dict = set(config.keys())
    keys_typehint = set(Config.__annotations__.keys())
    assert keys_dict == keys_typehint


def test_defaults():
    for value in config.values():
        v = value.to_string(value.default)
        assert isinstance(v, str)
        assert value.from_string(v) == value.default


def test_descriptions():
    for value in config.values():
        assert value.description is not None
