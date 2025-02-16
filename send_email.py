import os
import smtplib, ssl
import os


def sendEmail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "mondalsayandeep2004@gmail.com"
    password = os.getenv("PASSWORD_PF")
    receiver = "mondalsayandeep2004@gmail.com"
    context_msg = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context_msg) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


