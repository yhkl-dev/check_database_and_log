from config.config import GlobalConfig
from utils.email import send_email
from utils.common import scan_file_by_lines
import os

CONFIG = GlobalConfig().SPOTBUY


SUBJECT = "【T&T】SPOTBUY邮件发送自动监控"
CONTENT = """
Hi，
今日监控有SPOTBUY邮件发送失败，请处理，谢谢！

"""
# spotbuy邮件发送日志

ERROR_TEXT = "发送失败"


def check():
    for server in CONFIG.SERVER:
        # dirname = f"\\{server}\\e\\Track\\WinService\\Unisoft.WCF\\logs"
        dirname = "C:\\Users\\yangkai\\Desktop\\project-PRd\\check_database_and_log\\test_files"
        file_list = os.listdir(dirname)
        email_files = list(filter(lambda x: x.startswith("email"), file_list))
        email_files.sort(
            key=lambda x: os.path.getmtime(os.path.join(dirname, x))
        )
        lastest_file = email_files[-1]
        error_count, _ = scan_file_by_lines(os.path.join(dirname, lastest_file), ERROR_TEXT, 10)
        if error_count > 0:
            send_email(CONFIG.EMAIL, SUBJECT, CONTENT)

    print("check spotbuy done")
