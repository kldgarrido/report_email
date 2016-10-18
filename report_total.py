from util.mydate import calculate_total_day_range, calculate_last_seven_day_range
from util.dbhelper import execute_gasto_query, execute_ingreso_query
from util.emailhelper import prepareMessage, sendemail

def execute_report_total(subject):

    rangeTotal = calculate_total_day_range()

    gastos = execute_gasto_query(rangeTotal)
    ingreso = execute_ingreso_query(rangeTotal)

    html = prepareMessage(gastos, ingreso, rangeTotal)
    sendemail(html, subject)
    #print html