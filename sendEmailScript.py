import getpass                                                                                             
import smtplib                                                                        
HOST = "smtp.gmail.com"                                                                                 
PORT = 465
username = "username@email.com"                                                                             
password = getpass.getpass("Provide Gmail password: ")
server = smtplib.SMTP_SSL(HOST, PORT)

server.login(username, password) 
server.sendmail(
    "from@domain.com",       
     "to@domain.com",
      "An email from Python!",
    )
server.quit() 