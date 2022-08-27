from config.config import GlobalConfig
from utils.email import send_email
from utils.common import get_today, scan_file_by_lines

CONFIG = GlobalConfig().SK_PURGE_JOB_QUEUE


SUBJECT = "【TMS】SK_Purge_Job_Queue任务自动监控"
CONTENT = "Hi，SK_Purge_Job_Queue任务执行失败，请检查。"
# SK_Purge_Job_Queue

ERROR_TEXT = "failed"


def check():
    servers = [
        "120",
        "121",
    ]
    lastest_file = f"SK_Purge_Job_Queue_{get_today('%Y-%m-%d')}.log"
    for server in servers:
        target_file_path = f"\\{CONFIG.SERVER}\\e\\ScheduledTaskLog\\{server}\\{lastest_file}"
        error_count, _ = scan_file_by_lines(target_file_path, ERROR_TEXT, 4)
        if error_count != 0:
            send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
        print("Check 【TMS】SK_Purge_Job_Queue任务自动监控, done")
