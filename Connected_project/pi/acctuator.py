#importing smtp library
import smtplib

#this function is called when we want to send mail to someone saying the temprature is changed it takes argument to whom we want to mail
def sendmail(ToMailId):
    tomail=ToMailId
    #initializing smtp client
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #loggingin to my gmailid using id and password in order to sendmail
    server.login("youremailusername", "password")
    #message which needs to be sent
    msg = "Hello! temprature has been changed"
    server.sendmail("you@gmail.com", tomail, msg)
