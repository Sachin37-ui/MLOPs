import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("#$%^&*_8@gmail.com","#$%")
message="your model succesfully trained but didn't get the desired accuracy"
s.sendmail("Kendlyc#$4!8@gmail.com","sm0&%$@gmail.com",message)
print("mail sent")
s.quit()
