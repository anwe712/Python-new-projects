import time #import time module(This module provides various functions to manipulate time values.
import pygame

pygame.mixer.init()
print ("Welcome to the countdown timer")#print welcome message
print ("Please enter the number of seconds you want to countdown from:")#print message
seconds = int(input())#input seconds from user
while (seconds > 0):#while loop for countdown
    print (seconds)
    time.sleep(1)#sleep for 1 second
    seconds = seconds - 1  #decrement seconds
    # Load the sound file
    sound = pygame.mixer.Sound("countdownTimer/sound/boom-geomorphism-cinematic-trailer-sound-effects-123876.mp3")
    sound.play()   


print ("Time is up!") #print time is up message

