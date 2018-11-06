import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(time):
    mail_host = "smtp.gmail.com"
    mail_user = "my_gmail@@gmail.com"
    mail_pass = "my_email_password"
    mail_port = 587

    sender = 'sender_email_address@gmail.com'
    receivers= ['receiver_email_address@gmail.com']
    subject = 'garage door open too LONG alert'

    text = "Garage Door is open for "+str(time)+" minutes"
    email_text = """\
    From: %s
    To: %s
    content: %s
    """ % (sender, receivers,  text)
    message = MIMEText(email_text,'plain','utf-8')
    #
    # text = "Garage Door is open for "+str(time)+" minutes"
    # message = MIMEText(text,'plain','utf-8')
    message['Subject'] = Header(subject, 'utf-8')


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
