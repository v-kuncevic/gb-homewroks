import requests
from dateutil.parser import parse


def parsing_courses(src):
    url = f"https://open.er-api.com/v6/latest/{src}"  # Испаользую открытый ExchangeRate-API
    data = requests.get(url).json()  # Забираю данные в формате json
    if data["result"] == "success":
        time_current_course = parse(data["time_last_update_utc"])  # Там же забираю время
        exchange_rates = data["rates"]
        return time_current_course, exchange_rates
    else:
        return None


def recalculating_course(src, dst):
    time_current_course, exchange_rates = parsing_courses(src)  # Рассчёт курса
    return time_current_course, exchange_rates[dst]
