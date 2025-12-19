import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
SMTP_USER = "1152805923@qq.com"
SMTP_PASS = "tlsmqyyulccnifde"

def send_email_code(to_email, code):
    msg = MIMEText(f"您的验证码是：{code}，有效期5分钟")
    msg['Subject'] = "博客注册验证码"
    msg['From'] = SMTP_USER
    msg['To'] = to_email

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.send_message(msg)
    server.quit()
