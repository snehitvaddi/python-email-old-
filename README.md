# simple-python-email-sending-code
A simple code to send automatic emails direcly from python.

# In order to dend emails through python3 , we use SMTP Serever libraries.
#I want to see an acknowledgement if eamil has sent else notify me !!.. 

import smtplib
sender = 'v.snehith999@gmailcom'
receiver = 'v.pujithj@gmailcom'
message=""" From <email of sender> 
  To: To person <email of receiver>
  subject: SMTP HTML email test
  
This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1> """

#Note: (""")indicate multiline string.

try:
 server=smtplib.SMTP('smtp.gmail.com',587)
 server.sendmail(sender,receiver,message)
 print('Main has been sent successfully')
except SMTPException:
 print('Unable to send mail')
 
