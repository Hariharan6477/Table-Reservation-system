#contains functions to check if a mail id is valid
#and send a mail about the booking to both the user and manager

import re
#"smtplib” creates a Simple Mail Transfer Protocol client session object
import smtplib

global regex

#A regular expression (or RE) specifies a set of strings that matches it
#regular expression regex is used to check if the given mail_id is valid
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    #return True if the given mail_id (str) matches with the regular exp.
    #return True otherwise
    if(re.fullmatch(regex, email)): 
        return True
 
    else:
        return False    

def Send_Mail(user_mail_id, message_user, message_manager):
    
    #port number for gmail account is 587
    s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
    
    s.starttls() #smtp connection is put in tls mode for security reasons

    #authentication
    s.login("newragarestaurant@gmail.com", "fmfrwbiizqnmtixd")
    
    #sending the mail to both customer and manager
    s.sendmail("newragarestaurant@gmail.com", user_mail_id , message_user)
    s.sendmail("newragarestaurant@gmail.com", "managernewraga@gmail.com", message_manager)

    #terminates the smtp session
    s.quit() 
