from email.message import EmailMessage
from passfile import password
import ssl
import smtplib

email_sender = 'example@gmail.com'   #put the email address that will send the Email
email_password = password            #put your account generated password to be accessed 
email_receiver = 'example@gmail.com' #put the email that will receive the Email

subject = "mr.example please reply"
body = """I hope this email finds you well"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
