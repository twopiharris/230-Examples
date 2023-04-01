"""
sendmail demo.

Works with a standard gmail account.  It's best to make a custom account
for sending mails, because this technique can make the sending account a bit 
less risky.

"""


import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("yourAddress@gmail.com", "yourpassword")
#note that you may have an error here.  Log into your 
#gmail account through a browser and you may have a notification
#that your account was 'attacked' by an insecure app. That's this
#program.  There's a toggle to allow less secure apps, so turn that on
# this should be a throwaway account anyway.

sender = "addressOfSender@gmail.com"
recipient = "addressOfRecipient@gmail.com"
text = """
Your email message body here
"""
s.sendmail(sender, recipient, text)

