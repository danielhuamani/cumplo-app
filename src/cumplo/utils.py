from datetime import datetime, date, timedelta
from django.utils import timezone


def get_last_week():
    yesterday = timezone.localtime(timezone.now()) - timedelta(days=1)
    last_week = yesterday - timedelta(days=7)
    return last_week, yesterday


def convert_date_to_str(date):
    return date.strftime("%Y-%m-%d")


def convert_str_to_date(string, format_date='%d/%m/%Y'):
    date = datetime.strptime(string, format_date).date()
    return date
