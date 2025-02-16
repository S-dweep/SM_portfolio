import smtplib, ssl


def sendEmail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "mondalsayandeep2004@gmail.com"
    password = "dpcfxfsovtctywkf"
    receiver = "mondalsayandeep2004@gmail.com"
    context_msg = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context_msg) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


