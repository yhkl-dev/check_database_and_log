from utils.db import Database
from config.config import GlobalConfig
from utils.email import send_email

CONFIG = GlobalConfig().DATABASE_DISK_USEAGE

SUBJECT = "【T&T】数据库磁盘空间自动监控"
CONTENT = """
Hi，
今日监控数据库磁盘空间低于800G，请处理，谢谢！

"""


def check():
    want_result = 800
    db = Database(CONFIG.HOST, CONFIG.PORT, CONFIG.USERNAME, CONFIG.PASSWORD)
    res = db.query(CONFIG.SQL)
    disk_usage = int(res[0][0])

    if disk_usage > want_result:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
    print("check DATABASE_DISK_USEAGE done")
