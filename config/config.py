import os
from attrdict import AttrDict
from config.singleton import SingletonDecorator
import configparser


config = configparser.ConfigParser()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_JSON_FILE = "config.ini"
CONFIG_FILE_PATH = os.path.join(BASE_DIR, CONFIG_JSON_FILE)


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

    @property
    def TT_ON_LEAVE(self):
        return AttrDict({
            "HOST": self._config["TT_ON_LEAVE"]["SERVER"],
            "USERNAME": self._config["TT_ON_LEAVE"]["USERNAME"],
            "PASSWORD": self._config["TT_ON_LEAVE"]["PASSWORD"],
            "PORT": 1433,
            "SQL": self._config["TT_ON_LEAVE"]["SQL"],
            "EMAIL": self._config["TT_ON_LEAVE"]["EMAIL"].split(","),
        })

    @property
    def DATABASE_DISK_USEAGE(self):
        return AttrDict({
            "HOST": self._config["DATABASE_DISK_USEAGE"]["SERVER"],
            "USERNAME": self._config["DATABASE_DISK_USEAGE"]["USERNAME"],
            "PASSWORD": self._config["DATABASE_DISK_USEAGE"]["PASSWORD"],
            "PORT": 1433,
            "SQL": self._config["DATABASE_DISK_USEAGE"]["SQL"],
            "EMAIL": self._config["DATABASE_DISK_USEAGE"]["EMAIL"].split(","),
        })

    @property
    def CHINA_TRANSPORTATION_INTERFACE_LOG(self):
        return AttrDict({
            "SERVER": self._config["CHINA_TRANSPORTATION_INTERFACE_LOG"]["SERVER"],
            "FILE_PATH": self._config["CHINA_TRANSPORTATION_INTERFACE_LOG"]["FILE_PATH"],
            "EMAIL": self._config["CHINA_TRANSPORTATION_INTERFACE_LOG"]["EMAIL"].split(","),
        })

    @property
    def SPOTBUY(self):
        return AttrDict({
            "SERVER": self._config["SPOTBUY"]["SERVER"].split(","),
            "FILE_PATH": self._config["SPOTBUY"]["FILE_PATH"],
            "EMAIL": self._config["SPOTBUY"]["EMAIL"].split(","),
        })

    @property
    def WES(self):
        return AttrDict({
            "SERVER": self._config["WES"]["SERVER"],
            "FILE_PATH": self._config["WES"]["FILE_PATH"],
            "EMAIL": self._config["WES"]["EMAIL"].split(","),
        })

    @property
    def AUTO_SEND_EMAIL(self):
        return AttrDict({
            "SERVER": self._config["AUTO_SEND_EMAIL"]["SERVER"],
            "FILE_PATH": self._config["AUTO_SEND_EMAIL"]["FILE_PATH"],
            "EMAIL": self._config["AUTO_SEND_EMAIL"]["EMAIL"].split(","),
        })

    @property
    def LOAD_FILE_TRANSFER(self):
        return AttrDict({
            "SERVER": self._config["LOAD_FILE_TRANSFER"]["SERVER"],
            "FILE_PATH": self._config["LOAD_FILE_TRANSFER"]["FILE_PATH"],
            "EMAIL": self._config["LOAD_FILE_TRANSFER"]["EMAIL"].split(","),
        })

    @property
    def TMS_AND_POD_TIME_INTERFACE(self):
        return AttrDict({
            "SERVER": self._config["TMS_AND_POD_TIME_INTERFACE"]["SERVER"],
            "FILE_PATH": self._config["TMS_AND_POD_TIME_INTERFACE"]["FILE_PATH"],
            "EMAIL": self._config["TMS_AND_POD_TIME_INTERFACE"]["EMAIL"].split(","),
        })

    @property
    def SK_PURGE_JOB_QUEUE(self):
        return AttrDict({
            "SERVER": self._config["SK_PURGE_JOB_QUEUE"]["SERVER"].split(","),
            "TASK_NAME": self._config["SK_PURGE_JOB_QUEUE"]["TASK_NAME"],
            "EMAIL": self._config["SK_PURGE_JOB_QUEUE"]["EMAIL"].split(","),
        })

    @property
    def SK_INTERFACE_COST(self):
        return AttrDict({
            "SERVER": self._config["SK_INTERFACE_COST"]["SERVER"].split(","),
            "TASK_NAME": self._config["SK_INTERFACE_COST"]["TASK_NAME"],
            "EMAIL": self._config["SK_INTERFACE_COST"]["EMAIL"].split(","),
        })

    @property
    def SK_FILE_CLEANUP_PROCESS(self):
        return AttrDict({
            "SERVER": self._config["SK_FILE_CLEANUP_PROCESS"]["SERVER"].split(","),
            "TASK_NAME": self._config["SK_FILE_CLEANUP_PROCESS"]["TASK_NAME"],
            "EMAIL": self._config["SK_FILE_CLEANUP_PROCESS"]["EMAIL"].split(","),
        })
