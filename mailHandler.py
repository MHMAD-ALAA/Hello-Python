"""if you want to use this code don't forgot to change the (personally dependant) parts"""
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'your_email_address'  # personally dependant
EMAIL_PASSWORD = 'your_email_password'  # personally dependant

msg = EmailMessage()
msg['Subject'] = 'hello from mhmad-alaa'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'receiver_email'   # personally dependant

"""sending pdfs"""
msg.set_content("It's me,\nmohamed alaa a computer engineering student who just wanna be a kind and a good person. "
                "\nwhat a bout you? \n\n\n "
                "it's the last one hoda, Thanks alot for your help!\nalways hope you find the mail well (sorry), "
                "Our chat will discuss if us are well or not, but now is the mail check time.")

with open('hash_code.PDF', 'rb') as file:
    file_data = file.read()
    file_name = file.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

"""sending images"""
with open('BEB.png', 'rb') as file:
    file_data = file.read()
    file_name = file.name
    file_type = imghdr.what(file_name)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


"""more optimal way for adding the email address and passwords"""
"""
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
"""
