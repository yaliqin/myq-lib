import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# from os import path
# import sys
# sys.path.append(path.abspath('/Users/ally/Documents/python/djangoMyq/myQ'))
# from django.conf.urls import url
# import from urls import check_door_status


def send_mail(time,user, password, url):
    mail_host = "smtp.gmail.com"
    mail_user = user
    mail_pass = password
    mail_port = 587

    sender = mail_user
    receivers= ['qinyali@gmail.com']
    subject = 'garage door open too LONG alert'

    message = MIMEMultipart('mixed')
    message['Subject'] = Header(subject, 'utf-8')

    text = "Garage Door is open for "+str(time)+" minutes"
    # email_text = text
    email_text = """\
    From: %s
    To: %s
    content: %s
    """ % (sender, receivers,  text)

    #
    # text = "Garage Door is open for "+str(time)+" minutes"

    # html = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <a href="%s" target="_blank">"please confirm to close door"</a>
    #     <p>Text and HTML</p>
    #   </body>
    # </html>
    # """%(url)

    html = """\
    <html>
      <head></head>
      <body>
        <a href=\"{0}\" target="_blank">please confirm to close door</a>
        <p>Text and HTML</p>
      </body>
    </html>
    """.format(url)

    # p1 = """\
    # <html>
    #   <head></head>
    #   <body>
    #     <a href=\""""
    # p2= url
    # p3="""\" target="_blank">"please confirm to close door"</a>
    #     <p>Text and HTML</p>
    #   </body>
    # </html>
    # """
    # html = p1+p2+p3



    print(url)
    print(mail_user, mail_pass)
    part1 = MIMEText(email_text, 'plain')
    part2 = MIMEText(html, 'html')

    # Record the MIME types of both parts - text/plain and text/html.
    message.attach(part1)
    message.attach(part2)



    try:
        #   first use insecure connection
        smtpObj = smtplib.SMTP(mail_host,mail_port)
        #   then update to secure connection with TSL protocol
        smtpObj.starttls()
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("email sent successfully")
    except smtplib.SMTPException:
        print("Error: email cannot be sent")


