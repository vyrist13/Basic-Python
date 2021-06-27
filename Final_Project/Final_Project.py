#Ref.:https://www.tutorialspoint.com/send-mail-with-attachment-from-your-gmail-account-using-python
#Ref.:https://www.codegrepper.com/code-examples/python/how+to+send+email+attachment+in+python

from email.mime import text
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders, message
from getpass import getpass

mail_content="""Hi there,
This is a test email using Python for Final Project.

Best regards,
Thoma
"""

#The mail addresses and password
sender_email="toma.saputra@gmail.com"
with open("receiver_list.txt","r") as file:
    receiver_email=file.read().replace("\n",",")
password=getpass("Type your password and press enter:")

#Setup the MIME
message=MIMEMultipart()
message["Subject"]="Final Project with Attachment"
message["From"]=sender_email
message["To"]=receiver_email #the subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content,'plain'))
filename="receiver_list.txt"
attachment=open("receiver_list.txt","rb")
p=MIMEBase("application","octate-stream")
p.set_payload((attachment).read())
encoders.encode_base64(p) #encode the attachment

#Add payload header with filename
p.add_header("content-disposition","attachment;filename=%s"% filename)
message.attach(p)

#Create SMTP session for sending the mail
session=smtplib.SMTP("smtp.gmail.com",587) #use gmail with port
session.starttls() #enable security
session.login(sender_email,password) #login with email and password
text=message.as_string()
session.sendmail(sender_email,receiver_email,text)
session.quit
print("Mail Sent")