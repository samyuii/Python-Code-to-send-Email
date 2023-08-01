# Python Code to send Email to everyone use module behind it


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "jainsamyak170@gmail.com"  # Enter your address
receiver_email = "31samyak@gmail.com"  # Enter receiver address
password = "rjtr dejn drrl ggfp"  # Replace this with the actual password for sender_email
message = "What is up man"
Subject: "Hi there"

# This message is sent from Python.
# IM SAMYAK

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
