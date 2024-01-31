import os
roboX=5
roboHP=100
roboBT=100
bombX=7
bombY=8
HP_add = 2
length = 10
score=0
coins=1
while True:
    os.system('cls')

    print("\n")
    if roboBT>0:
        for x in range(1, length + 1):
            if x == roboX:
                print("☃", end=" ")
            elif x == bombX:
                print("💣", end=" ")
            elif x == bombY:
                print("💣", end=" ")
            elif x == HP_add:
                print("🎔", end=" ")
            elif x == coins:
                print("💰", end=" ")                
            else:
                print(".", end=" ")
        print("\nHP: " , roboHP )
        print("battery: " , roboBT , "%" )
        print("score: " ,score)
        
        print("\n")
    

    
        
      
        option=input(">>>>> ")
  
        if option == "a" and roboX>1:
            roboX-=1
            roboBT-=1
        if option == "d" and roboX<10:
            roboX+=1  
            roboBT-=1   
        if roboX==bombX:
            roboHP-=10
            bombX=0   
        if roboX==bombY:
            roboHP-=10  
            bombY=0
        if roboX==HP_add:
            roboHP+=10
            if roboHP>100:
                roboHP=100

            HP_add=0      
        if roboX==coins:
            score+=10
            coins=0        
        if option == "x":
            os.system("cls")
            print("bye")
            break   
    else:
        print("out of battery, Game OVER") 
        break       

        

    #HW1: frontier check right - check
    #HW2: place second bomb - check
    #HW3*: place some hearts -> +HP 
    #HW4*: place some coins -> +score
    #HW5*: add variables: state of bomb, coins