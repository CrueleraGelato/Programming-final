# CG, WW, MW, LK Build the game Final :(
name = input("What is your name?")
in_bathroom = False
in_hall = False
in_cafeteria = False
in_artroom = False
in_classroom = False
inventory = []
print("Masen")

# the next code works do not change it except for writing in the print statement
class_choice = int(input("1. Pick up the muffin on the teachers desk\n 2. Look through the backpack\n 3. Grab the pencil on the desk\n 4. Go to the hall\n What do you want to do: "))

if class_choice == 1:
    print("Masen write about picking the muffin up")
    inventory.append("Muffin") 
    print(inventory)
elif class_choice == 2: 
    print("masen write about looking through the backpack")
elif class_choice == 3: 
    print("Masen write about grabbing the pencil")
elif class_choice == 4:
    print("Masen write about going to the hall.")
    in_hall = True
else:
    print("That is not one of the options.")

if in_hall == True: 
    hall1 = print(input("1. Go back into the classroom\n 2. Go into the art room\n 3. Go into the bathroom\n 4. Go into the cafeteria\n What is your choice:"))
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
        print("Masen write cafeteria")
        in_cafeteria = True
else:
    if in_hall != 1 or in_hall != 2 or in_hall != 3 or in_hall != 4:
        print("That is not an option")











    







