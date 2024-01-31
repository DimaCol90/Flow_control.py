import os
from time import sleep
from random import randint
rx = 5
bx = -1
by = -1
tx=5
ty=3
score=0
option=""
while option !="x":

    os.system('cls')

    for y in range(1, 11):
        for x in range(1, 11):
            if x == rx and y == 10:
                print("R", end=" ")
            elif x == bx and y == by:
                print("⦿", end=" ")  
            elif x == tx and y == ty:
                print("🎯", end="")    
            
            else:
                print(".", end=" ")
        print()
    print("\nscore: ",score)    
    sleep(0.05) 
    
    if by!=-1:
        by-=1  
        if bx == tx and by == ty:
            ty=randint(1,7)
            tx=randint(1,10)
            by= -1
            score+=1          
            
        continue
    option=input(">>>>> ")
    if option == "a" and rx>1:
        rx-=1  
    if option == "d" and rx<10:
        rx+=1        
    if option == " ": 
        bx=rx
        by=9      