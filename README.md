# simple-python-email-sending-code
A simple code to send automatic emails direcly from python

import smtplib
sender = 'v.snehith999@gmailcom'
receiver = 'v.pujithj@gmailcom'
message=""" From <email of sender> 
  To: To person <email of receiver>
  subject: SMTP Automatic mail"""
  
#Note: (""")indicate multiline string.

try:
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.sendmail(sender,receiver,message)
 print('Main has been sent successfully')
except SMTPException:
 print('Unable to send mail')
 
