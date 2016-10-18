from  datetime import timedelta, datetime
import calendar


def calculate_last_seven_day_range():
    last_seven_day = datetime.today() - timedelta(days=7)
    today = datetime.today()

    str_fecha1 = last_seven_day.strftime("%Y-%m-%d")
    str_fecha2 = today.strftime("%Y-%m-%d")

    return (str_fecha1, str_fecha2)


def calculate_day_of_month_range():
    today = datetime.today()
    range =  calendar.monthrange(today.year,today.month)

    str_fecha1 = str(today.year)+"-"+str(today.month)+"-"+"01"
    str_fecha2 = datetime.today().strftime("%Y-%m-%d")

    return (str_fecha1, str_fecha2)


def calculate_total_day_range():
    str_fecha1 = "2016-06-02"
    today = datetime.today()
    str_fecha2 = today.strftime("%Y-%m-%d")
    return (str_fecha1, str_fecha2)
