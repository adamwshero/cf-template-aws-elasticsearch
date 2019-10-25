import logging
import logging.config
import os
import shared.log_config as lconfig


class BaseContext:
    def __str__(self):
        return f"({self.__class__.__name__}):{str(self.__dict__)}"

    @staticmethod
    def get_toggle(key: str):
        return bool(os.environ.get(key, None))

    @staticmethod
    def configure_logging():
        logging.config.dictConfig(lconfig.get_log_config(
            os.environ.get("LogLevel", "INFO")))

    def configure_settings(self):
        raise NotImplementedError(
            "No function configure_settings was implemented")

    def configure_services(self):
        raise NotImplementedError(
            "No function configure_services was implemented")

    def __init__(self):
        self.configure_logging()
        self.configure_settings()
        self.configure_services()
