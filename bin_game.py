#BINARY GAME V1
#This game was created by louis griffiths
#type 
"""
Created on Tue Nov  7 15:48:11 2017

@author: louis
"""
from random import randint

num1=randint(1, 1000)  # Integer from 0 to 1
bnum1=bin(num1)
sbnum1=str(bnum1)

print("what is ",num1," in binary")

myanswer = "0b"+input( 'What is your answer? '  ) 


if myanswer==sbnum1:
    print ("CORRECT!")
else:
     print("WRONG!")