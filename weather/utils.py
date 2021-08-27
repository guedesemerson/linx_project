from datetime import datetime


def filter_weather_by_date(date, response_weather):
    list_weather = []

    if date == '':
        return response_weather

    for row in response_weather:
        date_time_list = datetime.strptime(row['dt_txt'], "%Y-%m-%d %H:%M:%S")
        date_list = str(datetime.date(date_time_list))
        if date == date_list:
            list_weather.append(row)

    return list_weather
