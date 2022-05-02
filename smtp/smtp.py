import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart("alternative")
msg["Subject"] = 'Theme'
msg.attach(MIMEText('Body of letter', "plain"))


def send_mail(email, password, FROM, TO, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(FROM, TO, str(msg))
    server.quit()


"""
while True:
    send = send_mail(
        'from@gmail.com',
        'fromemailpassword,
        'sendername@gmail.com',
        'to@gmail.com',
        msg
    )
    time.sleep(5)
"""
