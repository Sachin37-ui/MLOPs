import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("tendlysachin8@gmail.com","Sarthak2@15")
message="model training is failed"
s.sendmail("tendlysachin8@gmail.com","sm026552@gmail.com",message)
print("mail sent")
s.quit()
