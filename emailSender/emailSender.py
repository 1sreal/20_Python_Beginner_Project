from email.message import Emailmessage
import ssl
import smtplib

email_sender = 'niibenedict123@gmail.com'

email_password = 'ypiiolxbdwodevij'

email_receiver ='fogocix713@prolug.com'

subject = 'Python journey' 

body = """
I really wanna push through but no buts....

"""
em = Emailmessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body) 

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465 context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
