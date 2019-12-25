import datetime
from dateutil.relativedelta import relativedelta


def get_date(date, fmt='%Y-%m-%d'):
    return str2date(date, fmt)


def get_today(date):
    return date


def get_yesterday(date):
    return add_days(date, -1)


def get_tomorrow(date):
    return add_days(date, 1)


def get_min_date():
    return datetime.date(1900, 1, 1)


def get_max_date():
    return datetime.date(2999, 12, 31)


def add_days(date, days=1):
    return date + datetime.timedelta(days)


def add_months(date, months=1):
    return date + relativedelta(months=months)


def add_years(date, years=1):
    return date + relativedelta(years=years)


def date2str(date, fmt='%Y-%m-%d'):
    return datetime.date.strftime(date, fmt)


def str2date(date, fmt='%Y-%m-%d'):
    return datetime.datetime.strptime(date, fmt).date()
