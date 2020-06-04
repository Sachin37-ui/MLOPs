import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "tendlysachin8@gmail.com"
host_pass = "sachiN19#98"
guest_address = "sm026552@gmail.com"
subject = "Regarding failure of modelone.py"
content = '''Hello, 
				Developer this is an email regarding to your last commit. It seems that your rebuild.py is  working properly and it get desired accuracy.
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')


