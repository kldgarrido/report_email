from util.emailsetting import report
from report_total import execute_report_total
from report_month import execute_report_month
from report_last_seven_days import execute_report_last_seven_days

subject_total = report['subject_total']
subject_month = report['subject_month']
subject_lastsevendays = report['subject_lastsevendays']

execute_report_total(subject_total)
execute_report_month(subject_month)
execute_report_last_seven_days(subject_lastsevendays)




