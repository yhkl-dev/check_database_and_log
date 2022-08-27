from utils.common import scan_file_by_lines, get_yesterday
from utils.email import send_email
from config.config import GlobalConfig

CONFIG = GlobalConfig().WES

SUBJECT = "【T&T】WES接口自动监控"
CONTENT = """
Hi，
今日监控有WES返回日志异常，请查看，谢谢！

"""
# 监控WES系统是否有正常传输叫号信息至追鹰系统，是否有报错

ERROR_TEXT = "记录WES返回日志异常"


def check():
    lastest_file = f"WESlog{get_yesterday('%Y%m%d')}.txt"
    print(">>>", lastest_file)
    target_file_path = f"\\{CONFIG.SERVER}\\e\\WES\\WESService\\{lastest_file}"
    error_count, _ = scan_file_by_lines(target_file_path, ERROR_TEXT, 8)
    if error_count != 0:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
    print("Check WES, done")
