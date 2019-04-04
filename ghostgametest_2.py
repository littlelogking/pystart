# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:43:51 2015


@author: louis
"""

# Ghost Game

from random import randint

def scoref():
    result = score
    return result

    


print('Ghost Game')

feeling_brave = True

score = 0

while feeling_brave:
    safe_door = randint(1, 10)   
    print('ten doors ahead...')    
    print('a ghost behind nine .')    
    print('which door do you open?'  )
    door = input( ' 1, 2, 4, 5, 6, 7, 8, 9, 10 or 3? '  ) 
    door_num = int(door) 
    if door_num < safe_door:
        print( 'GHOST!')
        feeling_brave = True
        print('You enter the next room.')
        print('Game over! You scored',score)
        score = 0
    else:
        print('No Ghost!')
        score=score+1
        print('Move on to the next room')
        
    print (scoref())
      
    if door_num > safe_door:
        print( 'GHOST!')
        feeling_brave = False
        print('Game over! You scored',score)
        score = 0
    else:
        print('No Ghost!')
        score=score+1
        print('Move on to the next room')
 