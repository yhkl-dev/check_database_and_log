from utils.common import get_yesterday, scan_file_by_lines
from utils.email import send_email
from config.config import GlobalConfig

CONFIG = GlobalConfig().CHINA_TRANSPORTATION_INTERFACE_LOG

SUBJECT = "【T&T】中交接口自动监控"
CONTENT = """
Hi，
今日监控中交接口传输异常，请处理，谢谢！

"""

# 中交接口日志 JobLog2022-08-27.log
# 8/27/2022 8:35:16 PM
# 智运开放平台接口服务:执行成功！
# 8/27/2022 8:35:16 PM
# 智运开放平台车辆能源类型接口服务:执行成功！

ERROR_TEXT = "执行失败"


def check():
    lastest_file = f"JobLog{get_yesterday()}.log"
    target_file_path = f"\\{CONFIG.SERVER}\\Log4\\{lastest_file}"
    error_count, _ = scan_file_by_lines(target_file_path, ERROR_TEXT, 8)
    if error_count != 0:
        send_email(CONFIG.EMAIL, SUBJECT, CONTENT)
    print("Check 中交接口, done")
