class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._settings = {
                "max_items": 50,
                "discount_rate": 0.1,
                "debug_mode": True
            }
        return cls._instance

    def get_settings(self):
        return self._settings

def get_config():
    return Config().get_settings()