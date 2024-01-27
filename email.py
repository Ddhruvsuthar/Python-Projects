import email

import ssl 
import smtplib

email_sender = 'bitcoinlately255@gmail.com'
email_password = 'bitcoinlately481632'

email_recevier = 'yalowit668@evvgo.com'

subjet = 'just trying out'
body = 'just me and you'

em = email.message()
em ['From'] = email_sender
em['To'] = email_recevier
em['subject'] = subjet
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_recevier,em.as_string())




