import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

while True:
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    sender_email = input("Please provide your preferred email address: ")

    if re.match(email_pattern, sender_email):
        print("Valid email address!")
        break
    else:
        print("Invalid email address. Please try again.")

receiver_email = 'jmwread@yahoo.com'
request_type = input("Please specify what type of request you are making (deletion, creation, or editing): ")
subject = input("Please describe your full issue or question here with as much detail as possible: ")

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Request Type'] = request_type
message['Subject'] = subject

message_text = "Hello,\n\nPlease address the following request:\n\nRequest Type: {}\n\n{}\n\nThank you.".format(
    request_type, subject)

message.attach(MIMEText(message_text, 'plain'))

# Set up your email server and authentication
smtp_server = 'smtp.gmail.com'
smtp_port = 465
email_address = 'jmwread3@gmail.com'
email_password = 'Spacecowboy123!'

server = None  # Initialize the server variable

try:
    # Establish a connection with the email server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Log in to your email account
    server.login(email_address, email_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

except Exception as e:
    print("Error occurred while sending the email:", str(e))

finally:
    if server is not None:  # Check if the server variable is defined
        # Close the connection
        server.quit()
        