# Server - SMTP
# @wthoutjc
import smtplib
from decouple import config

def get_email_server():
    '''
    Create an instance of email server
    Returns
        server - SMTP instance
    '''
    server = (
        smtplib.SMTP_SSL if config('EMAIL_SSL') else smtplib.SMTP)(
            config('EMAIL_HOST'),
            config('EMAIL_PORT')
        )
    