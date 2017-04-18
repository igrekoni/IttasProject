from datetime import datetime
from math import fabs


def counterHelper():
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
