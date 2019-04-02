# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

def details():
    global email_pass,email_user, email_send
    email_user = input('Please enter your email:')
    email_pass = input('Please enter your Password:')
    email_send = input('Please enter recipient:')


def login():

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user, email_pass)

def send():
    message = input ('What would you like the message to be?')
    server.sendmail(email_user, email_send, message)
    print ('Message sent!!!')


def main():
    details()
    login()
    send()
    server.quit()
