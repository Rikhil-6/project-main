# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:48:18 2022
Thanks Khai
@author: acer
"""
import re
import time
import enchant

d = enchant.Dict("en_SG")
# countdown func.
def countdown(t,player):    
    while t:
        mins, secs = divmod(t, 60)
        if secs!=4 and secs!=2:
            timer = '{:02d}'.format(secs)        
            print(timer+'\n')
        elif secs==4:
            print('Get Ready!\n')
        elif secs==2:
            print('Get Set!\n')
        time.sleep(1)
        t -= 1
      
    print(f'GO {player}')

def word_check(word,character):
    word=word.lower()
    return(word[0]==character and d.check(word))

def award_pts(dic,player_lose_num):
    keys=list(dic.keys())
    for i,k in enumerate(keys):
        if i==player_lose_num:
            pass
        else:
            dic[k]+=1


while True:
    c=input('Letter (1 from A to Z): ')
    if re.match('[a-z]',c.lower()) and len(c)==1:
        c=c.lower()
        break
    else:
        print('Invalid Character. Only 1 English alphabet allowed.')
            
while True:
    n=input('Number of players (Min 2; Max 5): ')
    if n.isdigit()and 1<int(n)<6:
        n=int(n)
        break 
    else:
        print('Invalid input.\nPlease enter an integer less than 6 and more than 1')
        
    
rounds=input('Number of Rounds to go (Default 3; Max 10): ')
if rounds.isdigit() and int(rounds)<=10:
    rounds=int(rounds)
else:
    print('Default number chosen.')
    rounds=3

print('\nPlayer name order matters!')      
dic={}

while True:
    pl=[]
    for e in range(0,n):
        p=input(f'Player {e+1} name: ')
        pl.append(p)
    if len(set(pl))==n:
        for p in pl:
            dic[p]=0
        break
    else:
        print('Player names must be different')

print('\n')

countdown(5,list(dic.keys())[0])

rounds_played=0
while rounds_played<rounds:
    players=list(dic.keys())
    for e in range(0,n):
        print(f'\nStarts with {c}')
        player=players[e]
        w=input(f"{player}'s word: ")
        if word_check(w,c):
            print('Accepted!')
        else:
            print(f'Oops! {player} has lost!\n')
            rounds_played+=1 
            award_pts(dic,e)
            for k,v in dic.items():
                if v!=1:
                    print(f'{k} now has {v}pts')
                else:
                    print(f'{k} now has {v}pt')
            print('\n')
            if rounds_played<rounds:
                countdown(5,players[(e+1)%n])
                       
print('Thanks for Playing!')            
            
    




