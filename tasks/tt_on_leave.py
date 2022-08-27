from utils.db import Database
from config.config import GlobalConfig
from datetime import datetime
from utils.email import send_email

CONFIG = GlobalConfig().TT_ON_LEAVE

SUBJECT = "【T&T】离职接口自动监控"
CONTENT = """
Hi，
今日监控离职接口未运行，请处理，谢谢！
"""


def check():
    current_date = datetime.now()
    db = Database(CONFIG.HOST, CONFIG.PORT, CONFIG.USERNAME, CONFIG.PASSWORD)
    res = db.query(CONFIG.SQL)
    db_exec_result_date = datetime.strptime(res[0][0], "yyyy-MM-dd HH:mm:ss")

    if current_date != db_exec_result_date:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
    print("check TT_ON_LEAVE done")
