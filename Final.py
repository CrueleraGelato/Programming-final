# CG, WW, MW, LK Build the game Final :(
in_bathroom = False
in_hall = False
in_cafeteria = False
in_artroom = False
in_classroom = False
inventory = []
hall1 = """"""
print("Masen")

# the next code works do not change it except for writing in the print statement
class_choice = int(input("1. Pick up the muffin on the teachers desk\n2. Look through the backpack\n3. Grab the pencil on the desk\n4. Go to the hall\nWhat do you want to do: "))
while True:
    if class_choice != 1 or class_choice != 2 or class_choice != 3 or class_choice != 4:
        if class_choice == 1:
            print("Masen write about picking the muffin up")
            inventory.append("Muffin")
        elif class_choice == 2:
            print("masen write about looking through the backpack")
        elif class_choice == 3:
            print("Masen write about grabbing the pencil")
            inventory.append("Pencil")
        elif class_choice == 4:
            print("Masen write about going to the hall.")
            in_hall = True
    elif class_choice.isnumeric():
            print("That is not an option.")
    break

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
    print("You walk over and try the door. Its locked, you might need something to open the lock.")
    in_cafeteria = True
else:
    """"""







