import smtplib
sender = 'v.snehith999@gmailcom'
receiver = 'v.pujithj@gmailcom'
message=""" 
From <email of sender> 
 To: To person <email of receiver>
 subject: SMTP Automatic mail
 <h>THIS IS HEAD</h>
 <b>THSI IS BODY</b>
"""
  
#Note: (""")indicate multiline string.

try:
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login("sender_email","Sender_password")
 server.sendmail(sender,receiver,message)
 print('Main has been sent successfully')
except SMTPException:
 print('Unable to send mail')
server.quit()
