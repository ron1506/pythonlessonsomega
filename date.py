import math


class Date(object):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, date: str):
        list_date = date.split(".")
        self.day = int(list_date[0])
        self.month = int(list_date[1])
        self.year = int(list_date[2])

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __add__(self, other):
        days1 = Date.get_days_from_date(self)
        if type(other) == Date:
            days2 = Date.get_days_from_date(other)
            total_days = days1 + days2
        else:
            total_days = days1 + other
        return Date.get_date_from_days(total_days)

    @staticmethod
    def get_days_from_date(date):
        return date.year * 365 + Date.get_sum_days_in_month(date.month) + date.day

    @staticmethod
    def get_sum_days_in_month(month):
        sum_days_in_months = 0
        for i in range(month - 1, 0, -1):
            sum_days_in_months += Date.days_in_month[i]
        return sum_days_in_months

    @staticmethod
    def get_date_from_days(total_days):
        ezer = total_days / 365
        new_year = math.floor(ezer)
        new_month = 0
        if math.ceil(ezer) == math.floor(ezer):
            new_year -= 1
            total_days = 365
            new_month = 12
        else:
            total_days %= 365
        if total_days <= Date.days_in_month[1]:
            new_month = 1
        else:
            total_days -= Date.days_in_month[1]
            for i in range(2, 12):
                if total_days <= Date.days_in_month[i]:
                    new_month = i
                    break
                else:
                    total_days -= Date.days_in_month[i]
            # for i in range(1, 12):
            #     total_days -= Date.days_in_month[i]
            #     if total_days <= Date.days_in_month[i+1]:
            #         new_month = i
            #         break
        new_days = total_days
        date_list = [str(new_days), str(new_month), str(new_year)]
        date_str = ".".join(date_list)
        return Date(date_str)

    def __sub__(self, other):
        days1 = Date.get_days_from_date(self)
        days2 = Date.get_days_from_date(other)
        return abs(days1 - days2)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year
