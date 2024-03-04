from email.mime.text import MIMEText

from email.mime.image import MIMEImage

from email.mime.application import MIMEApplication

from email.mime.multipart import MIMEMultipart

import smtplib

import os

user = "your email id"
password = "your app password"


# initialize connection to our
# email server, we will use gmail here

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

contact_name="your contact name"


# Login with your email and password

smtp.login(user, password)

def message(subject="Python Notification",

            text="", img=None,

            attachment=None):

    # build message contents

    msg = MIMEMultipart()

    # Add Subject

    msg['Subject'] = subject

    # Add text contents

    msg.attach(MIMEText(text))
    return msg


msg = message("Good!", "Hi there!")

# Make a list of emails, where you wanna send mail

to = ["recipient_mailid"]


# Provide some data to the sendmail function!

smtp.sendmail(from_addr="hello@gmail.com",

              to_addrs=to, msg=msg.as_string())
  
