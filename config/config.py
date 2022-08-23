import json
import os
from attrdict import AttrDict
from config.singleton import SingletonDecorator
import configparser


config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_JSON_FILE = "config.json"
CONFIG_FILE_PATH = os.path.join(BASE_DIR, CONFIG_JSON_FILE)


def read_config(config_file_path: str) -> AttrDict:
    with open(config_file_path, "r") as config:
        return AttrDict(json.loads(config.read()))


@SingletonDecorator
class GlobalConfig:

    def __init__(self) -> None:
        self._config = configparser.ConfigParser()
        self._config.read(CONFIG_FILE_PATH)
        print(self._config)

    @property
    def email_info(self):
        return AttrDict({
            "SERVER": self._config["EMAIL"]["SERVER"],
            "FROM": self._config["EMAIL"]["FROM"],
        })
