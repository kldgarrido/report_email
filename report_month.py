from util.mydate import calculate_day_of_month_range
from util.dbhelper import execute_gasto_query, execute_ingreso_query
from util.emailhelper import prepareMessage, sendemail

def execute_report_month(subject):

    rangeTotal = calculate_day_of_month_range()

    gastos = execute_gasto_query(rangeTotal)
    ingreso = execute_ingreso_query(rangeTotal)

    html = prepareMessage(gastos, ingreso, rangeTotal)
    sendemail(html, subject)