import smtplib
from typing import List
from email.utils import make_msgid, formatdate
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPRecipientsRefused, SMTPAuthenticationError, SMTPSenderRefused, SMTPException
from config.config import GlobalConfig
from email.mime.text import MIMEText

EMAIL = GlobalConfig().EMAIL


def send_email(email_address: List[str], email_subject: str, email_message: str):
    info = {
        "server": EMAIL.SERVER,
        # "server": "172.18.250.9"
    }
    smtp_server = info['server']
    msg = MIMEMultipart('mixed')
    msg['Subject'] = email_subject
    msg['From'] = EMAIL.FROM
    # msg['From'] = "test.mail@cn.ab-inbev.com"
    msg['To'] = ",".join(email_address)
    msg['Reply-to'] = EMAIL.FROM
    msg['Message-id'] = make_msgid()
    msg['Date'] = formatdate()
    texthtml = MIMEText(email_message, 'html')
    msg.attach(texthtml)
    try:
        client = smtplib.SMTP_SSL(smtp_server)
        client.connect(smtp_server, 25)
        # client.login(username, password)
        client.sendmail(EMAIL.FROM, email_address, msg.as_string())
        # client.sendmail("test.mail@cn.ab-inbev.com", email_address, msg.as_string())
        client.quit()
    except SMTPRecipientsRefused:
        print('Email delivery failed, invalid recipient')
    except SMTPAuthenticationError:
        print('Email delivery failed, authorization error')
    except SMTPSenderRefused:
        print('Email delivery failed, invalid sender')
    except SMTPException as e:
        print(f'Email delivery failed, {e}')
    except Exception as e:
        print(e)
