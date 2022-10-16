# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:56:08 2022

@author: acer
"""

import re
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
"""
num=-123 
n=str(num)
if n[0]=='-':
    r=int(n[0]+n[-1:0:-1])
else:
    r=int(n[-1::-1])
print(r)"""

#Max Change Calculator!!!

arr=[1,1]

#Decimal to Roman
"""
def to_Roman(number):
    dic={1:'I',4:'IV',5:'V',9:'IX',10:'X',
         40:'XL',50:'L',90:'XC',100:'C',
         400:'CD',500:'D',900:'CM',1000:'M'}
    number=str(number)
    res=''
    for i,e in enumerate(number):
        n=(int(e)*(10**(len(number)-i-1)))
        if n in dic:
            res+=dic[n]
        elif 1<n<4:
            res+=n*dic[1]
        elif 5<n<9:
            res+=dic[5]+(n-5)*dic[1]
        elif 10<n<40:
            res+=n*dic[10]
        elif 50<n<90:
            res+=dic[50]+((n-50)//10)*dic[10]
        elif 100<n<400:
            res+=n//100*dic[100]
        elif 500<n<900:
            res+=dic[500]+((n-500)//100)*dic[100]
        elif n>1000:
            res+=dic[1000]*(n//1000)       
    print(res)
        
to_Roman(247)"""
#Mark 1

#Maze Solving- learn about queues etc

"""
#HANGMAN
word=input('Word to guess: ')
for _ in range(0,10):
    print('\n')
if word.isalpha():
    word=word.lower()
    pass
else:
    raise ValueError('''No digits/ foreign characters allowed. 1 word and letters only.''')
guess= ['_'] * len(word)
print(' '.join(guess))
hangman=['','[]','\n'.join(['|','|','|','|','[]']),
         '\n'.join(['____','|','|','|','|','[]']),
         '\n'.join(['____','|*','|','|','|','[]']),
         '\n'.join(['____','|* +','|','|','|','[]']),
           '\n'.join(['____','|* +','|  o','|','|','[]']),
           '\n'.join(['____','|* +','|  o','|  ^','|','[]']),
           '\n'.join(['____','|* +','|  o','|  ^','|  ^','[]'])]
num=0
man=hangman[num]
while ''.join(guess)!=word and man!=hangman[-1]:
    letter=input('Letters Only: ')
    letter=letter.lower()
    old=guess.copy()
    for i,e in enumerate(guess):
        if word[i]==letter:
            guess[i]=letter 
            print(guess)
    if guess==old:
        num+=1
        man=hangman[num]
        print(man)
    else:
        print(' '.join(guess))

if man==hangman[-1]:
    print('Lost!')
    print(f'The word was {word}')
else:
    print('WON!!')
"""

"""
#List Comprehension

print(list(i for i in range(10) if i%2==0))
print([(x,y) for x in range(1,4) for y in range(0,20)])
# to have a constant number repeated a number of times
print([0 for i in range(100)])


#also check up on generator objects!!
"""

"""                                           
#Multiple assignement: Useful for swapping var

a, b = 1, 2
a,b = b,a
print(a,b)"""

"""
#Ternary operator

# =============================================================================
# x= (val If true) if (condition) else (val If false)
# print(x)
# =============================================================================

#E.g.

x= 1 if 2>3 else 0
print(x)

# no special operators etc -> unlike '?' / ':' in JS"""

#Zip function -> useful to know ya know

#*args -> in functions; unpacks list/tuple/ collection of items etc (positional)
#**kwargs -> akin to args; but unpacks it and uses the keys (accepts dic only)
# as the name of the args

"""
#SORT BY KEY

lst=[[1,2],[3,3]]
lst.sort(key= lambda x: x[1])

# where key takes a function which returns the index in a list/ collection to 
# sort by"""

"""
#Itertools
-> cool thing to know man"""

"""
#Cows and Bulls
#https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

import random
n=str(random.choice(range(1000,10000)))
print(f'To guess a {len(n)} digit number')
game=True 
tries=0
while game:
    tries+=1
    g=input('Guess: ')
    while len(g)!=len(n) or g.isdigit()==False:
        print('Invalid. Guess again')
        g=input('Guess: ') 
    cows=0
    bulls=0
    for e in range(0,len(n)):
        if n[e]==g[e]:
            cows+=1
        else:
            bulls+=1
    print('Cows:',cows)
    print('Bulls:',bulls)
    if cows==4:
        print(f'\nNumber Guessed! {tries} tries needed.')
        game=False """


#Sort and determine the best <cars> based on a number of factors

#import pandas as pd


#df=pd.read_excel(r'C:\Users\acer\Downloads\SG_Car.xlsx')
"""
#print(df.head())
#print(df.info())
colsa=['Full name','Engine capacity','Compression ratio','Power',
       'Top speed','Fuel consumption']
colsb=['Full name','CO2 emission']
df_h=df[colsa]
df_l=df[colsb]

dic={}
for car in df['Full name']:
    dic[car]=0

g=[]
for e in range(1,len(df_h.columns)):
    f=(sorted(set(filter(lambda x: x!='unknown',list(df_h.iloc[:,e])))))
    ff=f[-10:]
    g.append(ff)
x=0
car=df_h
while x<5:
    y=0
    for r in car.loc[:,colsa[x+1]]: 
        if r in g[x]:
            try:
                dic[list(dic.keys())[y]]+=1 
            except:
                pass
        y+=1
    x+=1

h=[]    
for e in range(1,len(df_l.columns)):
    f=(sorted(set(filter(lambda x: x!='unknown',list(df_l.iloc[:,e])))))
    ff=f[:9]
    h.append(ff)

s=0
car=df_l
while s<1:
    t=0
    for r in car.loc[:,colsb[t+1]]: 
        if r in h[s]:
            try:
                dic[list(dic.keys())[t]]+=1 
            except:
                pass
        t+=1
    s+=1

for k,v in dic.items():
    if v in [5,6]:
        print(df_h[df['Full name']==k])"""

"""
from datetime import datetime as dt

#1 <Oldschool>
l1=dt.now()
n=[]
for e in range(1,10000000):
    n.append(e**2)
l2=dt.now()
l=l2-l1
#longest time

#2 <Generator Objects>
x1=dt.now()
n1=list(map(lambda x:x**2,range(1,10000000))) 
#slightly faster <virtually instant when only the generator object is created>
x2=dt.now()
x=x2-x1
print(l.total_seconds(),x.total_seconds())

#3 <List Comprehension>
lc1=dt.now()
res=[num**2 for num in range(1,10000000)]
lc2=dt.now()
print((lc2-lc1).total_seconds())
#slightly slower than 2 <abt .1s>"""

f='This dog runs faster than the other dog dude!'

# =============================================================================
# x=list(range(0,10))
# y=list(map(lambda x: 2**x,x))
# import matplotlib.pyplot as plt
# 
# fig, ax= plt.subplots(1,2)
# ax[1].plot(x,y)
# ax[0].plot(y,y)
# =============================================================================


#https://towardsdatascience.com/the-cardio-of-audio-cbe310d94b48


#import librosa 
#import pandas as pd
#import matplotlib.pyplot as plt
#data, sample_rate = librosa.load(r"C:\Users\acer\Downloads\Wonderland.wav",sr=None)
"""
x=list(range(0,len(data)))
#plt.plot(x,data)
import numpy as np
import math
# =============================================================================
# ratio=0.1
# res=np.abs(np.fft.fft(data))
# 
# plt.plot(np.linspace(0,sample_rate,len(res))[:int(len(res)*ratio)]
#          ,res[:int(len(res)*ratio)])
# plt.xlabel('Freq (Hz)')
# =============================================================================
# =============================================================================
# 
# def to_scale(n,big=max(data),small=min(data)):
#     return (n-small/big-small)*100
# fn=np.vectorize(to_scale)
# new_data=fn(data)
# #plt.plot(list(range(0,len(new_data))))
# 
# def draw(number,mid,upper,lower):
#     if number>mid:
#         return('+'*math.ceil(int((number-mid)/(upper-mid)*20)))
#     elif number<mid:
#         return('-'*math.ceil(int((number-mid)/(lower-mid)*20)))
#     else:
#         return('O')
# print('GO!')
# for e in new_data:
#     print(draw(e,200,300,100))                  #progressing.
#                                                 #just have to link
#                                                 #music with points
# =============================================================================

res=np.fft.rfft(data)

ratio=sample_rate/len(res)
l=1000
plt.plot(list(np.linspace(0,sample_rate,len(res)))[:int(l/ratio)],res[:int(l/ratio)])

df=pd.DataFrame(res)
df['Real']=(np.vectorize(np.real)(res))
#print(df.groupby(df['Real']).apply(lambda x: int(x>0)).count())
"""

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\Maths.csv")
# print(df.head())
# print(df.info())
# #df.boxplot(['G1','G2','G3'],by='age')    
# #df.plot.scatter(x='G1',y='G2',s=df['G3'].apply(lambda x: x*20),marker='^')
# 
# dfa=df.groupby('age').mean()
# dfa.plot.bar(y=['G1','G2','G3'],figsize=(12,9))
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"https://raw.githubusercontent.com/fivethirtyeight/superbowl-ads/main/superbowl-ads.csv")
# def replace(x):
#     if x==True:
#         x=1 
#     else:
#         x=0
#     return x
# for e in ['funny','celebrity','use_sex','animals']:
#     df[e]=df[e].apply(replace)
# df=df.groupby('year')
# plt.style.use('ggplot')
# df['use_sex'].mean().plot()
# df['funny'].mean().plot()
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\NOAA Earthquaqe since 1600.csv")
# df=df.drop(['Date','Hours','Minutes','Name','Latitude','Longitude',
#             'Damage $Mill','Injuries','Id'],axis=1)
# df=df.dropna()
# df=df.set_index('Year')
# df['Magnitude'].plot(marker='*',figsize=(16,9),label='Magnitude')
# df['Deaths'].apply(lambda x:x/10000).plot(marker='^',figsize=(16,9),label='Deaths (tens of thousands)')
# plt.legend()
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\penguin_size.csv")
# df=df.dropna()
# 
# df.plot.scatter(x='flipper_length_mm',y='body_mass_g',
#                 c=df['sex'].map({'MALE':'blue','FEMALE':'red'}))
# df.boxplot(by=['species','island'],column='flipper_length_mm',figsize=(12,5))
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\StudentsPerformance.csv")
# print(df.info())
# #h=df.groupby(['gender','race/ethnicity','parental level of education']).mean()
# #print(h.boxplot())
# r={'group A':'red','group B':'orange','group C':'green','group D':'blue',
#    'group E':'black'}
# g={'male':'blue','female':'red'}
# """
# df.plot.scatter('reading score','math score',c=df['gender'].map(g),
#                 s=df['writing score'].map(lambda x: x*1.5),figsize=(12,10),
#                 label='writing score')"""
# fig, ax=plt.subplots(nrows=2,ncols=2,figsize=(18,11))
# df.boxplot(column='math score',by='parental level of education',ax=ax[0,0])
# df.boxplot(column='reading score',by='parental level of education',ax=ax[0,1])
# df.boxplot(column='reading score',by='parental level of education',ax=ax[1,0])
# plt.tight_layout()
# =============================================================================

"Seaborn next, But first"
"""
def alt_chr(string,title=True):
    '''input string to alternate characters.
title is either set to True/False.By default, title is true E.g:
    alt_chr('string')       >> StRiNg
    alt_chr('string',False) >> sTrInG'''
    if title:
        rem=0 
    else:
        rem=1
    res=''
    x=0
    for e in string:
        if re.match('[a-zA-Z]',e):
            if x%2==rem:
                res+=e.upper()
            else:
                res+=e.lower()
            x+=1
        else:
            res+=e
    return res
print(alt_chr('''Srsly tho it's mindboggling how some ppl 
              will just go to "WhY dO tHeY oBjeCtIfY tHeM lIkE tHiS?"''',
0))"""

"sns"

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\total-air-passenger-departures.csv")
# pf=df.pivot_table(index='Year',columns='Month',values='Number')
# norm = pf.apply(lambda x: (x-x.mean())/x.std(), axis = 1)#normalise by row
# plt.figure(figsize=(15,15))
# sns.heatmap(norm.tail(21),cmap='turbo',lw=0.1,linecolor='k')          
# =============================================================================
    
# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\total-air-passenger-departures-by-country.csv")
# df=df.dropna()
# pf=(df.pivot_table(index='Country',columns=['Year'],values='value')) 
# norm = pf.apply(lambda x: (x-x.mean())/x.std(), axis = 0)#normalise by column
# plt.figure(figsize=(25,8))
# sns.heatmap(norm,cmap='turbo')
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\oil-database.csv")
# #sns.boxplot(data=df,x='Operator Name',y='All Costs')
# #print(df.info())
# #df.boxplot(by='Year',column='All Costs')
# pf=df.pivot_table(index='Year',columns='Month',values='All Costs')
# norm = pf.apply(lambda x: (x-x.mean())/x.std(), axis = 0)
# sns.heatmap(norm,cmap='turbo')
# =============================================================================

# =============================================================================
# df=pd.read_csv(r"C:\Users\acer\Downloads\archive (5)\causes-of-accidents-by-severity-of-injury-sustained.csv")
# #plt.figure(figsize=(20,12))
# df_fatal=(df[df['accident']=='FATAL'].groupby('year').sum())
# #print(df_fatal)
# #df_fatal.plot.bar()
# #plt.title('Fatalities Per Year')
# 
# plt.figure(figsize=(16,9))
# print(df.head())
# pf=df[df['accident']=='FATAL'].pivot_table(index='cause',columns='year',values='number')
# norm = pf.apply(lambda x: (x-x.mean())/x.std(), axis = 0)
# sns.heatmap(norm,cmap='turbo',lw=0.1,linecolor='k')
# 
# #print(df[df['cause']=='Using PMD to Travel on Road'].groupby('year').sum())
# =============================================================================

"""
# Monty (python) Hall Problem
import random 

switch=0
games=0
for e in range(0,100000):
    games+=1
    car=(random.choice([1,2,3]))
    choice=(random.choice([1,2,3]))
    n=[car,choice]
    goat=[1,2,3]
    for e in range(0,2):
        try:
            goat.remove(n[e])
        except ValueError:
            pass
    if len(goat)==2:
        random.shuffle(goat)
        goat=[goat[0]]
    else:
        pass
    new_choice=[1,2,3]
    new_choice.remove(choice)
    new_choice.remove(goat[0]) 
    new_choice=new_choice[0]   
    
    if new_choice==car:
        switch+=1 
    else:
        pass
print(switch/games)"""

"""#DIY Calendar
import datetime 

def checkLeap(year):
    if (year%400==0) or (year%100!=0 and year%4==0):
        return True
    else:
        return False 

def Calendar(input_year):
    "accepts years after 1600"
    if input_year<1600:
        return 'Invalid Year.'
    else:
        leap=[31,29,31,30,31,30,31,31,30,31,30,31]
        not_leap=[31,28,31,30,31,30,31,31,30,31,30,31]
        first_day=(datetime.datetime(input_year,1,1).weekday())
        days={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
        mths=['Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']
        if checkLeap(input_year):
            months=leap 
        else:
            months=not_leap
        day=first_day
        year={}
        x=0
        for m in months:
            week={'Mon':[],'Tue':[],'Wed':[],'Thu':[],
                  'Fri':[],'Sat':[],'Sun':[]}
            for date in range(1,m+1):
                for k in days:
                    if day%7==k:
                        week[days[k]].append(str(date))
                day+=1
            year[mths[x]]=week 
            x+=1
    print(f'Year: {input_year}\n')
    for m,w in year.items():
        print('\t',m)
        x=0
        for day,date in w.items():           
            if '1' in date:
                for e in range(0,7):
                    d=days[x%7]
                    
                    print(d,' '.join(w[d]))
                    x+=1
            else:
                x+=1
        print('\n')
    print(f'Year: {input_year}')
                
(Calendar(1965))"""

