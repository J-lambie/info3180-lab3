import smtplib
def sendemail(From,fromEmail,subject,message):
    fromname=From
    toname='INFO3180-Dummy'
    subject=subject
    fromaddr = fromEmail
    msg=message
    toaddr  = 'coding.testing.email@gmail.com'
    toaddrs  = 'coding.testing.email@gmail.com'
    message = """From: {} <{}>
    
    To: {} <{}>
    
    Subject: {}
    
    {}"""
    
    messagetosend = message.format(
    
                                 fromname,
    
                                 fromaddr,
    
                                 toname,
    
                                 toaddr,
    
                                 subject,
    
                                 msg)
    
    # Credentials (if needed)
    
    username = 'coding.testing.email@gmail.com'
    
    password = 'Test-ing'
    
    # The actual mail send
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    
    server.starttls()
    
    server.login(username,password)
    
    server.sendmail(fromaddr, toaddrs, messagetosend)
    
    server.quit()