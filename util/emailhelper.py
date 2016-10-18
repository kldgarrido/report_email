import smtplib
from smtplib import SMTPException
from credential import credential_email
from emailsetting import report
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import locale


locale.setlocale( locale.LC_ALL, '' )


def prepareMessageBodyTable(items):
    l = []
    sum = 0.0
    for item in items:

        line = "<tr>"
        line += "<td>" + str(item.name )+ "</td>"
        balance = locale.currency(float(item.value), grouping=True)
        line += "<td>" + balance  + "</td>"
        line += "</tr>"
        l.append(line)
        sum += float(item.value)

    line = "<tr>"
    line += "<td><Strong>" + "Total" + "</Strong></td>"
    balance = locale.currency(sum, grouping=True)
    line += "<td><Strong>" + balance + "</Strong></td>"
    line += "</tr>"
    l.append(line)

    return l


def prepareMessage(gastos, ingreso, rangeTotal):
    # Body Table
    lgastos = prepareMessageBodyTable(gastos)
    lingreso = prepareMessageBodyTable(ingreso)

    # template html
    f = open('util/week_email.html','r')
    html = f.read()
    f.close()

    # Insert BodyTable into Template
    temp = ''.join(lgastos)
    html = html.replace('<!-- bodytable->gastos -->',temp)
    temp = ''.join(lingreso)
    html = html.replace('<!-- bodytable->ingreso -->',temp)
    html = html.replace('<!-- bodytable->rango->total -->', '(Desde '+str(rangeTotal[0])+" hasta "+str(rangeTotal[1])+' )')

    return html


def sendemail(html, subject):
    try:
        user = credential_email['user']
        password = credential_email['password']
        email_to = report['email_to']
        port = report['port']

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = email_to

        # Create the body of the message (a plain-text and an HTML version).
        text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        serversmtp = report['serversmtp']
        server = smtplib.SMTP(serversmtp, port)
        server.starttls()
        server.login(user, password)

        #msg = message

        server.sendmail(user, email_to, msg.as_string())
        server.quit()

    except SMTPException:
        print "Error: unable to send email. "


#d_gastos = {'Nube':'5000', 'Ads':'2000'}
#d_ingreso = {'Curso Hablar en publico':'4000000', 'Curso Comunicacion Inteligente':'3000000'}
#html = prepareMessage(d_gastos, d_ingreso)
#sendemail(html)