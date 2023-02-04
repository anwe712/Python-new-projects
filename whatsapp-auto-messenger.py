import pywhatkit
import webbrowser
phone_no = input("Enter receiver(recipient) phone number :") #enter phone number with country code
message = input("Enter message you want to send :")#this is the message you want to send
print("Schedule time below when to send WhatsApp message to recipient:")#this is the time you want to send the message
time_in_hrs = int(input("- At What Hour :")) #enter hour in 24 hour format
time_in__min = int(input("- At What Minutes :")) #enter minutes
pywhatkit.sendwhatmsg(phone_no, message, time_in_hrs, time_in__min)
