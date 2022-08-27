import sys
from tasks import (auto_send_email, china_transportation_interface_log,
                   database_disk_usage, load_file_transfer,
                   sk_file_cleanup_process, sk_interface_cost,
                   sk_purge_job_queue, spotbuy, tms_and_pod_time_interface,
                   tt_on_leave, wes)  # noqa


def main(*args):
    for check_item in args:
        if check_item in [name for name in globals()]:
            globals()[check_item].check()


if __name__ == '__main__':

    main(*sys.argv[1:])
