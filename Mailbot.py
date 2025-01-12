import smtplib as s

ob =s.SMTP('smtp.gamil.com', 587)
ob.ehlo()
ob.starttls()
ob.login('girirajchaudhari1997@gmail.com','giriraj@1234')
subject="test pyhton"
body=" Python is best "
message="subject:{}\n\n{}".format(subject,body)
listadd=['girirajchaudhari1997@gmail.com',
         "swapnilchaudhari5504@gmail.com"]
ob.sendmail('girirajchaudhari1997@gmail.com',", ".join(listadd),message)
print("send mail successfully")
ob.quit()