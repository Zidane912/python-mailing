import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Zidane Alam'
email['to'] = SENDER_EMAIL
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'John Doe'}), 'html')
try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(TARGET_EMAIL, TARGET_PASSWORD)
        smtp.send_message(email)
        print('Email sent successfully')
except:
  print('ERROR EMAIL NOT SENT')