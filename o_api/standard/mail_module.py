import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 맥북은 터미널에 ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl 친다.


port = 587
smtp_server = "smtp.gmail.com"
sender_email = "wmoon0024@gmail.com"
receiver_email = "wmoon0024@gmail.com"
password = "disa wwwi xnho wuve"
message = "<h1>내용</h1>"

msg = MIMEText(message, 'html')
data = MIMEMultipart()
data.attach(msg)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, data.as_string())