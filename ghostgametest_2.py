# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:43:51 2015


@author: louis
"""

# Ghost Game

from random import randint
import sys

#FIXME


def scoref():
    result = score
    return result

def ghostdoor(score):
      print( 'GHOST!')
      feeling_brave = False
      print('You enter the next room.')
      print('Game over! You scored',score)
      return feeling_brave
      
def safedoor(score):
    print('No Ghost!')
    score=score+1
    print('Move on to the next room')
    return score
     
    

    


print('Ghost Game')

#TODO work through logic here
score = 0
feeling_brave = True
while feeling_brave:
    safe_door = randint(1, 10)   
    print('ten doors ahead...')    
    print('a ghost behind nine .')    
    print('which door do you open?'  )
    door = input( ' 1, 2, 4, 5, 6, 7, 8, 9, 10 or 3? '  ) 
    door_num = int(door) 
    
    if door_num > safe_door:
        ghostdoor(score)
    
    if door_num < safe_door:
       ghostdoor(score)
        
    else:
       score=safedoor(score)
        
      
    
        
 