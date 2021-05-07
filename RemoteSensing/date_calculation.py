import numpy as np


def cal_days_of_year(year, month, day):
    """
    cal the ith-day of the year
    input format: int
    return - total_days: ith-day of the year
             total_days_of_year:  the day number of the year

    """

    # https://blog.csdn.net/weixin_46198526/article/details/104105996
    day_of_second = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    days_of_month = (31, day_of_second, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # 累加前几个月的总天数
    total_days = sum(days_of_month[: month - 1])
    # 累加当月天数
    total_days += day
    # 计算这年一共有多少天
    total_days_of_year = sum(days_of_month)
    return total_days, total_days_of_year


def diff_two_days(date1, date2):
    """
    get the diff days of two day
    input format: "YYYYMMDD"
    """

    if int(date1) > int(date2):
        data1, date2 = date2, date1

    year1 = int(date1[0:4])
    year2 = int(date2[0:4])
    month1 = int(date1[4:6])
    month2 = int(date2[4:6])
    day1 = int(date1[6:8])
    day2 = int(date2[6:8])

    if year1 == year2:
        # calculate the relative
        diff_days = abs(cal_days_of_year(year1, month1, day1)[0] - cal_days_of_year(year2, month2, day2)[0])
    else:
        # 如果不是同一年，计算start year到end_year-1的所有天数 + end_year的到这天的天数 - start year的到这天的天数
        start_year = year1
        end_year = year2
        diff_days = 0
        for idx_year in np.arange(start_year, end_year):
            diff_days += cal_days_of_year(idx_year, 0, 0)[1]  # [1] refer the total days of the year

        # +end_year的到这天的天数 - start year的到这天的天数
        diff_days = diff_days - cal_days_of_year(year1, month1, day1)[0] + cal_days_of_year(year2, month2, day2)[0]
    return diff_days


'获得一天的前n天和后n天的日期'
from datetime import datetime, timedelta


def get_date(image_date, days=16):
    """
    Get the date of the first n days and the date of the next n days of the date
    refer:
    https://blog.csdn.net/liuzonghao88/article/details/88105309
    https://blog.csdn.net/evillist/article/details/50522505"""

    # you can get today:
    # date.today: YYYY-MM-D
    # datetime.now: 2019-02-25 10:56:58.609985

    # 格式化为 年月日 形式 2019-02-25
    year, month, day = image_date.split('-')
    start_date = (datetime(int(year), int(month), int(day)) - timedelta(days=days)).strftime(
        "%Y-%m-%d")  # 可以修改"%Y-%m-%d"成为你想要的时间格式 比如"%Y.%m.%d"等
    end_date = (datetime(int(year), int(month), int(day)) + timedelta(days=days)).strftime("%Y-%m-%d")
    print('start_date: ', start_date)
    print('end_date: ', end_date)
    return start_date, end_date
