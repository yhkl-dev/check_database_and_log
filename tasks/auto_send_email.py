from utils.common import scan_file_by_lines, get_yesterday
from utils.email import send_email
from config.config import GlobalConfig

CONFIG = GlobalConfig().AUTO_SEND_EMAIL

SUBJECT = "【T&T】SPOTBUY招标申请邮件发送自动监控"
CONTENT = """
Hi，
今日监控有招标申请邮件发送失败，具体信息如下，请处理，谢谢！

{content}
"""
# 监控是否有正常发送招标申请邮件至承运商

ERROR_TEXT = "邮箱发送失败"


def check():
    lastest_file = f"JobLog{get_yesterday()}.log"
    target_file_path = f"\\{CONFIG.SERVER}\\e\\Track\\Temp\\Log\\{lastest_file}"
    error_count, error_content = scan_file_by_lines(target_file_path, ERROR_TEXT, 8)
    if error_count != 0:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT.format(content=error_content))
    print("Check SPOTBUY招标申请邮件发送自动监控, done")
