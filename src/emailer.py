# Emailer Module for DiTing

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Emailer:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
                print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_daily_brief(self, user_email, brief_content):
        subject = "Your Daily Brief from DiTing"
        self.send_email(user_email, subject, brief_content)