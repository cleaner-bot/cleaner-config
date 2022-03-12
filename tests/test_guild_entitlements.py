from cleaner_conf.guild.entitlements import entitlements, Entitlements


def test_typehint():
    keys_dict = set(entitlements.keys())
    keys_typehint = set(Entitlements.__annotations__.keys())
    assert keys_dict == keys_typehint


def test_defaults():
    for value in entitlements.values():
        v = value.to_string(value.default)
        assert isinstance(v, str)
        assert value.from_string(v) == value.default


def test_descriptions():
    for value in entitlements.values():
        assert value.description is not None
