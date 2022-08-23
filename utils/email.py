

import smtplib
from typing import List
from email.utils import make_msgid, formatdate
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPRecipientsRefused, SMTPAuthenticationError, SMTPSenderRefused, SMTPException
from config.config import GlobalConfig

EMAIL = GlobalConfig().email_info


def send_email(email_address: List[str], email_subject: str, email_message: str):
    info = {
        "server": "smtpdm.aliyun.com"
    }
    smtp_server = info['server']
    msg = MIMEMultipart('mixed')
    msg['Subject'] = email_subject
    msg['From'] = EMAIL.FROM
    msg['To'] = ",".join(email_address)
    msg['Reply-to'] = EMAIL.FROM
    msg['Message-id'] = make_msgid()
    msg['Date'] = formatdate()

    try:
        client = smtplib.SMTP_SSL(smtp_server)
        client.connect(smtp_server, 465)
        # client.login(username, password)
        client.sendmail(EMAIL.FROM, email_address, msg.as_string())
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
