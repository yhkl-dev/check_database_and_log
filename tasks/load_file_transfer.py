from utils.common import get_yesterday
from utils.email import send_email
from config.config import GlobalConfig
import datetime
import os

CONFIG = GlobalConfig().LOAD_FILE_TRANSFER
SUBJECT = "【T&T】负载文件传输自动监控"
CONTENT = """
Hi，
今日监控有传输失败的负载，请处理，谢谢！
"""
# 避免有些负载文件一直传输报错，但未及时处理的情况。添加人工检查接口日


def check():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    file_path = f"\\{CONFIG.SERVER}\\e\\Track\\WebAPP\\TrackWebService\\Temp\\LoadError\\{current_year}\\{current_month}"
    file_list = os.listdir(file_path)

    curretn_day_file = list(filter(lambda x: datetime.fromtimestamp(
        os.path.getmtime(os.path.join(file_path, x))).date() == get_yesterday(), file_list))

    if len(curretn_day_file) > 0:
        send_email(CONFIG.SERVER, SUBJECT, CONTENT)

    print("check 负载文件传输自动监控 done")
