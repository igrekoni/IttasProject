from math import fabs, ceil
import re
from django.utils.html import strip_tags


def counterHelper():
    from datetime import datetime
    currentYear = datetime.today().year
    currentMonth = datetime.today().month
    currentDay = datetime.today().day

    zeroYear = 2015
    zeroMonth = 3
    zeroDay = 3

    targetYear = int(currentYear) - zeroYear
    targetMonth = int(fabs(int(currentMonth) - zeroMonth))
    targetDay = int(fabs(int(currentDay) - zeroDay))

    return targetYear, targetMonth, targetDay


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = ceil(count / 200.0)
    # read_time_sec = read_time_min * 60
    # read_time = str(datetime.timedelta(seconds=read_time_sec))
    # read_time = str(datetime.timedelta(minutes=read_time_min))
    return int(read_time_min)
