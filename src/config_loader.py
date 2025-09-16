import tomllib

_config = None

def get_config(path="config/settings.toml"):
    global _config
    if _config is None:
        with open(path, "rb") as f:
            _config = tomllib.load(f)
    return _config
