from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'jmwread3@gmail.com'
email_password = 'kwmvraeuwzqobpwi'

email_reciever = 'jmwread3@gmail.com'

subject = input('What type of issue is you ticket about? (deleting, editing, or new document): ')
body = input("Please describe with as much detail as possible the problem you are having: ")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())