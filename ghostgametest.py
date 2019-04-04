# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 08:43:51 2015


@author: louis
"""

# Ghost Game

from random import randint

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
    if door_num == ghost_door:
        print( 'GHOST!')
        feeling_brave = False
        score=score+1
    else:
        print('No ghost!')
        print('You enter the next room.')
print('Game over! You scored',score)
        
 