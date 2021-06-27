import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

sender_email="toma.saputra@gmail.com"
with open("receiver_list.txt","r") as file:
    receiver_email=file.read().replace("\n",",")
password=getpass("Type your password and press enter:")

message=MIMEMultipart("alternative")
message["Subject"]="Final Project"
message["From"]=sender_email
message["To"]=receiver_email

# Create the plain-text and HTML version of your message
text="""\
    Hi there,
    This message is sent from Python
    
    Best regard,
    Thoma"""
html="""\
    <html>
    <body>
    <p>Hi there,<br>
    This message is sent from Python<br>
    <br>
    Best regards,<br>
    Thoma
    </p>
    </body>
    </html>
    """

# Turn these into plain/html MIMEText objects
part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(
        sender_email,receiver_email,message.as_string()
    )