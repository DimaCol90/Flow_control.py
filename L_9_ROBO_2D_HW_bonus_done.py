import os

length = 10
height = 10

roboX = 5
roboY = 5

bombX = 7
bombY = 8

HP_add_X = 3
HP_add_Y = 4

coins_X = 8
coins_Y = 9

roboHP = 100
roboBT = 100
score = 0

while True:
    os.system('cls')

    print("\n")
    if roboBT > 0:
        for y in range(1, height + 1):
            for x in range(1, length + 1):
                if x == roboX and y == roboY:
                    print("☃", end=" ")
                elif x == bombX and y == bombY:
                    print("💣", end="")
                elif x == HP_add_X and y == HP_add_Y:
                    print("🎔", end=" ")
                elif x == coins_X and y == coins_Y:
                    print("💰", end="")
                else:
                    print(".", end=" ")
            print()

        print("HP: ", roboHP)
        print("battery: ", roboBT, "%")
        print("score: ", score)
        print()

        option = input(">>>>> ")

        if option == "a" and roboX > 1:
            roboX -= 1
            roboBT -= 1
        elif option == "d" and roboX < length:
            roboX += 1
            roboBT -= 1
        elif option == "w" and roboY > 1:
            roboY -= 1
            roboBT -= 1
        elif option == "s" and roboY < height:
            roboY += 1
            roboBT -= 1
        elif option == "x":
            os.system("cls" if os.name == 'nt' else 'clear')
            print("bye")
            break
        else:
            
            input("Invalid input. Try again. \nPress any button to continue: ")

        if roboX == bombX and roboY == bombY:
            roboHP -= 10
            bombX=0
            bomby=0

        if roboX == HP_add_X and roboY == HP_add_Y:
            roboHP += 10
            if roboHP > 100:
                roboHP = 100
            HP_add_X=0
            HP_add_Y=0    

        if roboX == coins_X and roboY == coins_Y:
            score += 10
            coins_X =0
            coins_Y=0
    else:
        print("Out of battery, Game Over")
        break