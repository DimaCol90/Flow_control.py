# app  / travel 

from os import system

destination = "Italy"
price_plane = 500
price_train = 150
transport_type=""
run=True

while run:
    system("cls")

    print("\n")
    print("############ MENU #############")
    print ("""
        1. Show prices
        2. Buy ticket
        3. cancel order
        4. total cost
        0. exit the app""")

    print("\n")


    option=int(input("choose-> "))

    if option ==1:
        system("cls")
        print(F'Destination: {destination}')
        print(f"place ticket cost: {price_plane}")
        print(f"train ticket cost: {price_train}")
        input("hit enter to continue...")

    if option ==2:
        print("select transportation type")
        print("1. plane")
        print("2. train")
        transport_type = int(input("choose-> "))
        seats = int(input("how many tickets? "))
        if transport_type ==1:
            cost= seats * price_plane
        elif transport_type ==2:
            cost=seats*price_train
        input("hit enter to continue...")

    if option == 3:
        seats = 0
        transport_type = 0 
        cost = 0
        input("hit enter to continue...")

    if option ==4:
        print(f"total cost: {cost}")
        input("hit enter to continue...")
    if option == 0:
        run=False
 



