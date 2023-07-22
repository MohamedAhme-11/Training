from smtplib import SMTP_SSL # while using gmail needs smtp to make connection , ssl to make it be secure 
from email.message import EmailMessage # for desging the email structure 
import os #using os power
import json #for using json file 
from mimetypes import guess_type #to get the type for every file i using 

class READ_INPUT:
    json_file = open("email.json") # read the json file 
    data_from_json_file = json.load(json_file) #load the data in the json file
    SENDER_EMAIL_sender = data_from_json_file["email"] #taking email info from data loaded
    EMAIL_PASSWORD_sender = data_from_json_file["password"] #taking password info from data loaded
    files_to_send = input("please enter the file : ")# loading all the files with all files type
class CREATE_MASSAGE(READ_INPUT):
    def Send_Mail(SENDER_EMAIL_sender, RECEIVER_EMAIL, EMAIL_PASSWORD_sender, SUBJECT, CONTENT, files_to_send):# function for sending the emails and receive all the email info 
        #formating my emails
        msg = EmailMessage()# create email message class for formating the email
        msg["From"] = SENDER_EMAIL_sender# saying the sender email
        msg["To"] = RECEIVER_EMAIL# saying the receiver email
        msg["Subject"] = SUBJECT# the email subject. the title of the email
        msg.set_content(CONTENT)# the email content 
        
        mime_type, encoding = guess_type(files_to_send)# will get from this line what type of data for every file 
        app_type, sub_type = mime_type.split("/")[0], mime_type.split("/")[1]#mime type the file type afterr the ""/" and the . , #apptype # the file is image or exceel and so on.. 

        with open(files_to_send, "rb") as binray_file:# open the file 
            file_data = binray_file.read()#read the file content
                # add attchemnt with type of data you are sending, app type like ex.image,sub type like ex.png
            msg.add_attachment(
            file_data, maintype=app_type, subtype=sub_type, filename=files_to_send
                    )
        #sending mail via smtp server #make connection
        with SMTP_SSL("smtp.gmail.com", 465) as smtp:#using the gmail and make connection with port number
            smtp.login(SENDER_EMAIL_sender, EMAIL_PASSWORD_sender)#login 
            smtp.send_message(msg)#sending the message created with its structure
            smtp.close()#close the connection 
        print("mail sent sucessfully")#after sending the mail sucessfully printing mail send sucessfully
class CALL_AND_FORMAT(CREATE_MASSAGE):
    object_from_create_message = CREATE_MASSAGE  
    RECEIVER_EMAIL = input("please enter the receiver email :")#reciver email
    SUBJECT = "Test"# email subject
    ## email content
    CONTENT = """ 
    HELLO 


    This mail for you just for test ,
    Thanks and regrads
    """
    object_from_create_message.Send_Mail(object_from_create_message.SENDER_EMAIL_sender, RECEIVER_EMAIL, object_from_create_message.EMAIL_PASSWORD_sender, SUBJECT, CONTENT, object_from_create_message.files_to_send)#calling the function
