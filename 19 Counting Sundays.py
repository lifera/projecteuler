'''

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def count_sundays():
    answer = 0
    last_week_day = 2
    days_in_month = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for year in range(1, 101):
        if year % 4 == 0:
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28

        for month in range(12):
            last_week_day += days_in_month[month] % 7
            if last_week_day > 7:
                last_week_day -= 7
            if last_week_day == 7:
                answer += 1
    print(answer)

count_sundays()