import smtplib
from email.mime.text import MIMEText

# import config

def send_mail(customer, dealer, rating, comments):
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = "ebe3f313452d08"
  password = "5a7cfbd54f9e30"
  message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

  sender_email = 'mail@example.com'
  receiver_email = 'mail@example2.com'
  msg = MIMEText(message, 'html')
  msg['Subject'] = 'Lexus Feedback'
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # Send email
  with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
