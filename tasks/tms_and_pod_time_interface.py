from utils.common import scan_file_by_lines, get_yesterday
from utils.email import send_email
from config.config import GlobalConfig

CONFIG = GlobalConfig().TMS_AND_POD_TIME_INTERFACE

SUBJECT = "【T&T】工厂POD传输自动监控"
CONTENT = """
Hi，
    今日监控工厂POD传输失败，请检查，谢谢！
"""
# 避免TMS进出厂时间与POD时间传输错误，但未及时处理的情况。添加人工检查接口日志后，减少对系统性能和业务操作的影响


ERROR_TEXT = "工厂POD传输失败"


def check():
    lastest_file = f"JobLog{get_yesterday()}.log"
    target_file_path = f"\\{CONFIG.SERVER}\\e\\Track\\Temp\\Log\\{lastest_file}"
    error_count, _ = scan_file_by_lines(target_file_path, ERROR_TEXT, 8)
    if error_count != 0:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
    print("Check 工厂POD传输自动监控, done")
