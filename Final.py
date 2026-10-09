# CG, WW, MW, LK Build the game Final :(
in_bathroom = False
in_hall = False
in_cafeteria = False
in_artroom = False
in_classroom = True
inventory = []
hall1 = """"""
muffin = False
backpack = False
classroom1 = """"""
pencil = False 
toothpick = False 
bath1 = """"""
print("Masen")
art1 = """"""
cafe1 =""""""

while True:
    class_choice = int(input("1. Pick up the muffin on the teachers desk\n2. Look through the backpack\n3. Grab the pencil on the desk\n4. Go to the hall\nWhat do you want to do: "))
    if class_choice != 1 or class_choice != 2 or class_choice != 3 or class_choice != 4:
        print("That is not an option.")
    elif class_choice.isnumeric():
            print("That is not an option.")
    else:
        if class_choice == 1:
            if ("Muffin") in inventory:
                print("You already have it.")
            else:
                print("Masen write about picking the muffin up")
                inventory.append("Muffin")
                muffin1 = print(input("1. Eat the muffin\n2. cut open the muffin\nWhat do you want to do:"))
                if muffin1 == 1: 
                    print("Masen write about dying from the muffin")
                elif muffin1 == 2: 
                    print("You need a knife to cut open the muffin")
        elif class_choice == 2:
            print("masen write about looking through the backpack")
        elif class_choice == 3:
            print("Masen write about grabbing the pencil")
            inventory.append("Pencil")
        elif class_choice == 4:
            print("Masen write about going to the hall.")
            in_classroom == False
            in_hall = True
        elif class_choice != class_choice.is_integer():
            print("That is not one of the options.")
        else:
            print("That is not an option.")
    else:
        """"""
    break 
if in_hall == True: 
    print("masen write about the hall")
    hall1 = print(input("1. Go back into the classroom\n2. Go into the art room\n3. Go into the bathroom\n4. Go into the cafeteria\nWhat is your choice:"))
if hall1 == 1:
    print("Masen write about going back into the classroom")
    in_classroom = True
elif hall1 == 2: 
    print("masen write about art room")
    in_artroom = True
if hall1 == 3: 
    print("Masen write about bathroom")
    in_bathroom = True
if in_hall == 4:
    print("You walk over and try the door. Its locked, you might need something to open the lock.")
    in_cafeteria = True
else:
    """"""


if in_artroom == True: 
    print("Masen write about the artroom")
    art1 = print(input("1. Pick up a toothpick\n 2. inspect a painting\n 3. Draw on the whiteboard\n 4. Go back into the hall\n What do you want to do:"))
if art1 == 1:
    print("Masen write about toothpick")
elif art1 == 2: 
    print("masen write about the painting")
if art1 == 3: 
    print("Masen write about whiteboard")
if art1 == 4:
    print("masen write about going to the hall")
    hall1 = True
else:
    """"""
if in_bathroom == True: 
    print("masen write about the bathroom")
    bath1 = print(input("1. Wash your hands\n2. fix the plumbing\n3.Grab the coin\n4. Go back into the hall\n What do you want to do:"))
if bath1 == 1:
    print("Masen write about washing your hands")
elif bath1 == 2: 
    print("masen write about the plumbing")
if bath1 == 3: 
    print("Masen write about grabbing coin")
    inventory.append("Silver Coin")
if bath1 == 4:
    print("masen write about going to the hall")
    hall1 = True
else:
    """"""

if in_cafeteria == True: 
    print("masen write about the cafe")
    cafe1 = print(input("masen write about 4 different choices"))
if cafe1 == 1:
    print("Masen write about #1")
elif cafe1 == 2: 
    print("masen write about #2")
if cafe1 == 3: 
    print("Masen write about #3")
if cafe1 == 4:
    print("masen write about going to the hall ")
    hall1 = True
else:
    """"""





