from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'niibenedict123@gmail.com'

email_password = 'ypiiolxbdwodevij'

email_receiver ='fogocix713@prolug.com'

subject = 'Python journey' 

body = """
I really wanna push through but no buts....

"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body) 

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

'''def replace_word():

    str = "I was a great person in future"
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the new word: ")
    print(str.replace(word_to_replace, word_replacement))
replace_word()