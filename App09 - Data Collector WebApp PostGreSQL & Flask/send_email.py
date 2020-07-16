from email.mime.text import MIMEText
import smtplib

def send_email(email, height, avg_height, count):
    #Update sender e-mail
    f_email = ""
    f_pass = ""
    t_email = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>{}</strong>. <br>Average height of all is <strong>{}</strong> and that is calculated out of <strong>{}</strong> people. <br> Thank you.".format(height, avg_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = t_email
    msg['From'] = f_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(f_email, f_pass)
    gmail.send_message(msg)