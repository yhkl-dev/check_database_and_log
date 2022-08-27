import datetime
import linecache
import os
from typing import Union


def get_line_count(filename: str) -> int:
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            buffer = f.read(1024 * 1)
            if not buffer:
                break
            count += buffer.count('\n')
    return count


def get_yesterday(format: str = None) -> str:
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    if format:
        return yesterday.strftime(format)
    return yesterday


def get_today(format: str = None) -> str:
    today = datetime.date.today()
    if format:
        return today.strftime(format)
    return today


def scan_file_by_lines(filename: str, error_text: str, line_counts: str) -> Union[int, str]:
    if not os.path.exists(filename):
        print(f'error, file {filename} not exist')
        return
    linecache.clearcache()
    line_count = get_line_count(filename)
    line_count = line_count - (line_counts - 1)
    error_count = 0
    error_content = ""
    for _ in range(line_counts):
        last_line = linecache.getline(filename, line_count)
        if error_text in last_line:
            error_count += 1
            error_content = last_line
        line_count += 1

    return error_count, error_content
