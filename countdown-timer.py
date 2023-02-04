#countdown timer project
import time #import time module(This module provides various functions to manipulate time values.
print ("Welcome to the countdown timer")#print welcome message
print ("Please enter the number of seconds you want to countdown from:")#print message
seconds = int(input())#input seconds from user
while (seconds > 0):#while loop for countdown
    print (seconds)
    time.sleep(1)#sleep for 1 second
    seconds = seconds - 1  #decrement seconds
print ("Time is up!") #print time is up message
