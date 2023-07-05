# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime
from calendar import monthrange


def parse_str(text: str):
    week, day, month = text.split()
    week = int(week[0])
    day = parse_day(day)
    month = parse_month(month)
    year = datetime.now().year
    days_count = monthrange(year, month)[1]
    week_counter = 0
    for i in range(1, days_count + 1):
        data = datetime(day=i, month=month, year=year)
        if data.weekday() == day:
            week_counter += 1
            if week_counter == week:
                return data


def parse_month(month: str) -> int:
    months = {'янв': 1, 'фев': 2, 'мар': 3, "апр": 4, "мая": 5, "июн": 6, "июл": 7, "авг": 8, "сен": 9,
              "окт": 10, "ноя": 11, "дек": 12}
    return months.get(month[:3], None)


def parse_day(day: str) -> int:
    match day.lower():
        case "понедельник":
            return 0
        case "вторник":
            return 1
        case "среда":
            return 2
        case "четверг":
            return 3
        case "пятница":
            return 4
        case "суббота":
            return 5
        case "воскресенье":
            return 6


if __name__ == '__main__':
    print(parse_str("1-й четверг ноября"))
    print(parse_str("3-я среда мая"))
