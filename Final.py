# WW, CG, LK, MW, CSP, Programming Final
# Masen did ALL of the print statements 
# Levi did ALL of the ASCII art 
# Carrera Debugged the entire code 
# William wrote almost all of the code 
import random
inventory = []
game_over = False
won = False
second_round = False
loop_number = 1
classroom_first_visit = True
bunny_approved_this_round = False
in_classroom = True
in_hall = False
in_bathroom = False
in_cafeteria = False
in_artroom = False
muffin_saved = False
backpack = False
pencil = False
toothpick = False
knife = False
muffin_key = False
lunch_token = False
sticker = False
marker = False
paintbrush = False
crayon = False
silver_coin = False
soap_key = False
paper_star = False
lunch_sticker = False
cafeteria_unlocked = False
bathroom_checked = False
games_played = 0
best_items = 0
last_items = 0
wins = 0
# Masen did ALL of the print statements 
name = input("What is your name: ").strip().capitalize()
print(f"Hello {name}! Welcome to our game!")

# William made all this code: 
def load_results():
    global games_played, best_items, last_items, wins

    try:
        with open("game_results.txt", "r") as file:
            lines = file.readlines()

        if len(lines) >= 4:
            games_played = int(lines[0].strip())
            best_items = int(lines[1].strip())
            last_items = int(lines[2].strip())
            wins = int(lines[3].strip())

    except (FileNotFoundError, ValueError):
        games_played = 0
        best_items = 0
        last_items = 0
        wins = 0


def save_results():
    with open("game_results.txt", "w") as file:
        file.write(str(games_played) + "\n")
        file.write(str(best_items) + "\n")
        file.write(str(last_items) + "\n")
        file.write(str(wins) + "\n")


def choose(options):
    for i, option in enumerate(options, 1):
        print(str(i) + ". " + option)

    while True:
        answer = input("> ").strip()

        if answer.isdigit():
            number = int(answer)

            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"{name}, please enter a valid number, you're better than this.")


def add_item(item):
    if item not in inventory:
        inventory.append(item)
        print(f"{name}, you collected: " + item + "!")


def show_inventory():
    if inventory:
        print("\nInventory:")

        for item in inventory:
            print("- " + item)
    else:
        print(f"{name}\nYour inventory is empty.")


def item_count():
    return min(len(inventory), 10)


def get_grade(count):
    if count >= 9:
        return "A"
    elif count >= 7:
        return "B"
    elif count >= 5:
        return "C"
    elif count >= 3:
        return "D"
    else:
        return "F"


def reset_loop_items():
    global muffin_saved, backpack, pencil, toothpick, knife, muffin_key
    global lunch_token, sticker, marker, paintbrush, crayon, silver_coin
    global soap_key, paper_star, lunch_sticker, cafeteria_unlocked, bathroom_checked

    inventory.clear()
    muffin_saved = False
    backpack = False
    pencil = False
    toothpick = False
    knife = False
    muffin_key = False
    lunch_token = False
    sticker = False
    marker = False
    paintbrush = False
    crayon = False
    silver_coin = False
    soap_key = False
    paper_star = False
    lunch_sticker = False
    cafeteria_unlocked = False
    bathroom_checked = False

# Levi made the bunny photo
def encounter_bunny():
    global game_over, won, bunny_approved_this_round

    print("\nA strange bunny appears in front of you!")
    print('Bunny: "Ohh, what have we got here?"')

    print(r"""&#x20;
                []     []
                [] \/ []
                ((|)_(|))
                /( : )\
               | |   | |
               | |   | |
                 b   b
""")
# Masen wrote the conversaiton with the bunny 
    if second_round:
        print('\nBunny: "You again? You really do want to leave, don\'t you?"')

        choice = choose([
            "Ask politely if you can leave",
            "Demand that the bunny move",
            "Ask if the bunny wants to play"
        ])

        if choice != "Ask politely if you can leave":
            print('\nBunny: "Hmm. I don\'t think you understand how this works."')
            print("The bunny disappears into the shadows.")
            return

        print(f'\n{name}: "Please, can I go home?"')
        print('Bunny: "Maybe. But tell me something first..."')
        print('"Why should I let you go?"')

        choice = choose([
            "Because you are scared of it",
            "Because you have learned your lesson",
            "Because you think it is funny"
        ])

        if choice != "Because you have learned your lesson":
            print('\nBunny: "That is not the answer I was hoping for."')
            print("The bunny disappears into the shadows.")
            return

        print(f'\n{name}: "I have learned my lesson. I just want to go home."')
        print('Bunny: "One last question..."')
        print('"What will you do if I let you leave?"')

        choice = choose([
            "Come back tomorrow",
            "Tell everyone about this place",
            "Leave quietly and never return"
        ])

        if choice == "Leave quietly and never return":
            print(f'\n{name}: "I will leave quietly and never come back."')
            print('Bunny: "Fine, I\'ll go if that\'s what you want."')
            print('Bunny: "You have earned the chance to leave."')
            print('Bunny: "Go to the main exit. Your way out is waiting."')
            bunny_approved_this_round = True

        else:
            print('\nBunny: "Then I suppose you are not ready yet."')
            print("The bunny vanishes into the darkness.")
# Levi did the ASCII art 
    else:
        choice = choose([
            "Hide",
            "Say hi",
            "Wave"
        ])

        if choice == "Hide":
            print(f"{name} hides behind a nearby object.")
        elif choice == "Say hi":
            print('You: "Hi!"')
        else:
            print(f"{name} waves at the bunny.")
            print("""
                (o.o)”/”
              |(____)
                |  |   
            """)
            print("""
                (o.o)”)”
              |(____)
                |  |   
            """)
            print("""
                (o.o)”/”
              |(____)
                |  |   
            """)
            print("""
                (o.o)”)”
              |(____)
                |  |   
            """)
        choice = choose([
            "Ask nicely to be let go",
            "Stand your ground",
            "Run away"
        ])

        if choice == "Ask nicely to be let go":
            print('You: "Please, can you let me go?"')
            print('Bunny: "Fine, I\'ll go if that\'s what you want"')
            bunny_approved_this_round = True

        elif choice == "Stand your ground":
            print('You: "I am not afraid of you!"')
            print('Bunny: "You are a feisty one! I like that!"')
            bunny_approved_this_round = True

        else:
            print("You run away, but the bunny catches up to you.")
            print("Your attempt has ended.")
            print(r"""
                (x.x)
              /(____)\
               /    \
            """)
            game_over = True


def check_bunny_encounter():
    if not second_round and random.randint(1, 10) == 1:
        encounter_bunny()
    elif second_round and random.randint(1, 10) == 1:
        encounter_bunny()

# Levi did the ASCII art 
def classroom():
    global game_over, muffin_saved, backpack, pencil
    global muffin_key, second_round, loop_number, in_classroom, bunny_approved_this_round
    global classroom_first_visit

    in_classroom = True
    display_entry = True

    while not game_over and in_classroom:
        print("\nCLASSROOM")

        if classroom_first_visit:
            print(f"{name} wakes up in an abandoned kindergarten classroom.")

            print(r"""
            (-.-) zzzZZ
          /(____)\
           /    \
        """)

            print(r"""
            ( ͡° ͜ʖ ͡° )
          /(________)\
           |        |
        """)

            classroom_first_visit = False

        elif display_entry:
            print(f"{name} enters the classroom.")

        display_entry = False
# Carrera wrote about the classroom loop 
        print("A muffin sits on the desk.")
        print("A backpack rests underneath the table.")
        print("The classroom door is slightly open.")

        options = [
            "Look at the muffin",
            "Inspect the backpack",
            "Pick up the pencil",
            "Go to the hall",
            "Check inventory"
        ]

        if muffin_saved and knife and not muffin_key:
            options.insert(3, "Cut the muffin with the knife")

        if muffin_key:
            options.insert(3, "Use the Muffin Key on the exit")

        choice = choose(options)
# Levi did the ASCII art 
        if choice == "Look at the muffin":
            print(r"""
           (^^^ ^^^)
            \|_|_|/
            """)

            muffin_choice = choose([
                "Eat the muffin",
                "Save the muffin",
                "Leave the muffin alone"
            ])
# Levi did the ASCII art 
            if muffin_choice == "Eat the muffin":
                print(f"\n{name} eats the muffin.")
                print("Everything goes dark.")
                print(f"{name}s attempt has ended.")
                print("""
                   (x.x)
                 /(____)\\
                  /    \\
                 """)
                game_over = True

            elif muffin_choice == "Save the muffin":
                muffin_saved = True
                print("You decide to save the muffin for later.")

            else:
                print("You leave the muffin on the desk.")
# Carrera wrote the classroom loop 
        elif choice == "Inspect the backpack":
            if not backpack:
                backpack = True
                print("\nInside the backpack is an empty lunchbox.")
                add_item("Lunch Token")
                print(f"{name} puts the empty lunchbox back.")
            else:
                print("The backpack is empty except for the lunchbox.")

        elif choice == "Pick up the pencil":
            if not pencil:
                pencil = True
                add_item("Pencil")
                print(f"{name} notices tiny termites crawling on it.")
            else:
                print(f"{name} has already picked up the pencil.")

        elif choice == "Cut the muffin with the knife":
            if muffin_saved and knife and not muffin_key:
                print(f"\n{name} carefully cuts open the muffin.")
                print("Something metallic glints inside.")
                muffin_key = True
                add_item("Muffin Key")
                print(f"{name} found the real Muffin Key!")
            else:
                print(f"{name} cannot do that yet.")
# Carrera wrote about the second round 
        elif choice == "Use the Muffin Key on the exit":
            if muffin_key:
                print(f"\n{name} unlocks the main exit with the Muffin Key.")
                print("The door opens, but there is only another classroom beyond it.")
                print(f"{name} steps through, and everything looks familiar, except a poster that lies on the wall saying: Those twitching ears have watched you roam…..find the bunny to make it home")
                print(f"{name}: What does that mean?")
                print(f"The seemingly still poster moves, {name} screams")
                print("Poster: find out....")
                print("The poster moves back to it's calm state")

                loop_number += 1
                second_round = loop_number >= 2
                bunny_approved_this_round = False

                display_entry = True

                if loop_number == 2:
                    print("\nSECOND LOOP")
                elif loop_number == 3:
                    print("\nTHIRD LOOP")
                else:
                    print(f"\nLOOP {loop_number}")

                print(f"{name} needs to find a way to escape for real.")
            else:
                print(f"{name} cannot use that key right now.")

        elif choice == "Go to the hall":
            in_classroom = False
            enter_room("hall")

        elif choice == "Check inventory":
            show_inventory()

# William wrote everything below: 
def enter_room(room):
    global in_hall, in_bathroom, in_cafeteria
    global in_artroom, in_classroom, game_over
    global bathroom_checked, cafeteria_unlocked

    in_classroom = room == "classroom"
    in_hall = room == "hall"
    in_bathroom = room == "bathroom"
    in_cafeteria = room == "cafeteria"
    in_artroom = room == "artroom"

    if room == "bathroom":
        bathroom_checked = True

        if random.randint(1, 20) == 1:
            print("\nThe bathroom door is locked.")
            in_bathroom = False
            in_hall = True
            return

    print(f"\n{name} enters the " + room.replace("_", " ") + ".")
    check_bunny_encounter()

    if not game_over:
        if room == "hall":
            hall()
        elif room == "bathroom":
            bathroom()
        elif room == "cafeteria":
            cafeteria()
        elif room == "artroom":
            artroom()


def hall():
    global game_over, in_classroom, in_hall, second_round

    in_hall = True

    while not game_over and in_hall:
        print("\nHALLWAY")
        print("The hallway is quiet. A trophy case stands against the wall.")
        print("The main exit is locked.")

        options = [
            "Look at the trophy case",
            "Go to the classroom",
            "Go to the art room",
            "Go to the bathroom",
            "Go to the cafeteria",
            "Try the main exit",
            "Check inventory"
        ]

        choice = choose(options)

        if choice == "Look at the trophy case":
            if not sticker:
                add_item("Sticker")
                print(f"{name} peels a sticker off the trophy case.")
                globals()["sticker"] = True
            else:
                print("The trophy case is empty of anything useful.")

        elif choice == "Go to the classroom":
            in_hall = False
            classroom()

        elif choice == "Go to the art room":
            in_hall = False
            enter_room("artroom")

        elif choice == "Go to the bathroom":
            in_hall = False
            enter_room("bathroom")

        elif choice == "Go to the cafeteria":
            in_hall = False

            if cafeteria_unlocked or "Toothpick" in inventory:
                enter_room("cafeteria")
            else:
                print("The cafeteria door is locked tight.")

            in_hall = True
# Carrera did the this loop: 
        elif choice == "Try the main exit":
            if second_round and bunny_approved_this_round:
                print("\nThe exit unlocks.")
                print(f"{name} steps outside into the fresh air.")
                print(f"{name} finally escaped!")
                game_over = True
                globals()["won"] = True

            elif (muffin_key or "Muffin Key" in inventory) and not second_round:
                print("The Muffin Key fits the lock.")
                print("The door leads you back to the classroom.")
                globals()["muffin_key"] = True
                in_hall = False
                classroom()

            elif "Soap Key" in inventory:
                print("The Soap Key does not fit the main exit.")

            else:
                print("The exit is locked. You need a key.")

        elif choice == "Check inventory":
            show_inventory()


def artroom():
    global in_artroom, cafeteria_unlocked
    global toothpick, marker, paintbrush, crayon

    in_artroom = True

    while not game_over and in_artroom:
        print("\nART ROOM")
        print("Drawings cover the walls. Art supplies are scattered everywhere.")

        choice = choose([
            "Look through the art supplies",
            "Take the toothpick",
            "Go to the hall",
            "Check inventory"
        ])

        if choice == "Look through the art supplies":
            if not marker:
                marker = True
                add_item("Marker")
            elif not paintbrush:
                paintbrush = True
                add_item("Paintbrush")
            elif not crayon:
                crayon = True
                add_item("Crayon")
            else:
                print(f"{name} has already searched the art supplies.")

        elif choice == "Take the toothpick":
            if not toothpick:
                toothpick = True
                add_item("Toothpick")
                print("It might be useful for a stubborn lock.")
            else:
                print(f"{name} already has the toothpick.")

        elif choice == "Go to the hall":
            in_artroom = False
            enter_room("hall")

        elif choice == "Check inventory":
            show_inventory()

# William did everything below: 
def bathroom():
    global in_bathroom, silver_coin, soap_key, paper_star

    in_bathroom = True

    while not game_over and in_bathroom:
        print("\nBATHROOM")
        print("The lights flicker above a cracked sink.")
        print("A broken pipe drips steadily.")

        choice = choose([
            "Search the sink",
            "Inspect the soap dispenser",
            "Look near the broken pipe",
            "Go to the hall",
            "Check inventory"
        ])

        if choice == "Search the sink":
            if not silver_coin:
                silver_coin = True
                add_item("Silver Coin")
                print(f"{name} finds a silver coin beside the drain.")
            else:
                print("There is nothing else in the sink.")

        elif choice == "Inspect the soap dispenser":
            if not soap_key:
                soap_key = True
                add_item("Soap Key")
                print("There is a tiny key hidden inside the dispenser.")
            else:
                print("The dispenser is empty.")

        elif choice == "Look near the broken pipe":
            if not paper_star:
                paper_star = True
                add_item("Paper Star")
                print("You find a folded paper star on the floor.")
            else:
                print("There is nothing else near the pipe.")

        elif choice == "Go to the hall":
            in_bathroom = False
            enter_room("hall")

        elif choice == "Check inventory":
            show_inventory()

# Carrera wrote this fuction 
def cafeteria():
    global in_cafeteria, cafeteria_unlocked, knife, lunch_sticker

    in_cafeteria = True

    if not cafeteria_unlocked:
        if "Toothpick" in inventory:
            print(f"\n{name} uses the toothpick to carefully open the cafeteria lock.")
            cafeteria_unlocked = True
        else:
            print("The cafeteria is locked.")
            in_cafeteria = False
            return

    print("\nCAFETERIA")
    print(f"The room is dark. {name} can barely make out the tables.")

    choice = choose([
        "Reach for the shiny object",
        "Turn on the lights",
        "Feel beneath the tables",
        "Go to the hall",
        "Check inventory"
    ])

    while not game_over and in_cafeteria:
        if choice == "Reach for the shiny object":
            print(f"\n{name} reaches into the darkness and gets a small cut.")
            print("You pull your hand back and decide to be more careful.")

        elif choice == "Turn on the lights":
            print("\nThe lights flicker on.")
            print("A knife lies on a nearby table.")

            if not knife:
                take_knife = choose([
                    "Take the knife",
                    "Leave the knife"
                ])

                if take_knife == "Take the knife":
                    knife = True
                    add_item("Knife")

            else:
                print("The knife is already in your inventory.")

        elif choice == "Feel beneath the tables":
            if not lunch_sticker:
                lunch_sticker = True
                add_item("Lunch Sticker")
                print(f"{name} finds a sticker stuck beneath a table.")
            else:
                print(f"{name} finds nothing else under the tables.")

        elif choice == "Go to the hall":
            in_cafeteria = False
            enter_room("hall")
            return

        elif choice == "Check inventory":
            show_inventory()

        if in_cafeteria and not game_over:
            choice = choose([
                "Reach for the shiny object",
                "Turn on the lights",
                "Feel beneath the tables",
                "Go to the hall",
                "Check inventory"
            ])

# William did the rest: 
def play_game():
    global game_over, won, second_round, loop_number, classroom_first_visit
    global bunny_approved_this_round
    global muffin_saved, backpack, pencil, toothpick
    global knife, muffin_key, lunch_token, sticker
    global marker, paintbrush, crayon, silver_coin
    global soap_key, paper_star, lunch_sticker
    global cafeteria_unlocked, bathroom_checked
    global in_classroom, in_hall, in_bathroom
    global in_cafeteria, in_artroom
    global games_played, best_items, last_items, wins

    inventory.clear()
    game_over = False
    won = False
    second_round = False
    loop_number = 1
    classroom_first_visit = True
    bunny_approved_this_round = False
    muffin_saved = False
    backpack = False
    pencil = False
    toothpick = False
    knife = False
    muffin_key = False
    lunch_token = False
    sticker = False
    marker = False
    paintbrush = False
    crayon = False
    silver_coin = False
    soap_key = False
    paper_star = False
    lunch_sticker = False
    cafeteria_unlocked = False
    bathroom_checked = False
    in_classroom = True
    in_hall = False
    in_bathroom = False
    in_cafeteria = False
    in_artroom = False

    print("\nKINDERGARTEN: THE DEMON BUNNY")
    print("--------------------------------")
    print(f"{name} wakes up in an abandoned kindergarten.")
    print("Dust hangs in the air, and the walls are covered in faded drawings.")
    print("A muffin sits on the desk in front of you.")
    print("A pencil lies beside it, and a backpack rests under the table.")
    print("The classroom door is slightly open.")

    while not game_over:
        if in_classroom:
            classroom()
        elif in_hall:
            hall()
        elif in_bathroom:
            bathroom()
        elif in_cafeteria:
            cafeteria()
        elif in_artroom:
            artroom()
        else:
            classroom()
            
    games_played += 1
    last_items = item_count()
    best_items = max(best_items, last_items)

    print("\n--------------------------------")

    if won:
        wins += 1
        print(f"{name} ESCAPED!")
        print("The abandoned kindergarten fades away.")
        print(f"{name} realizes the whole experience was a simulation.")
        print("The principal gives you an A for effort.")
# Levi did the ASCII art 
        print(r"""
        (u _u)
        /)  (\
       | (  ) |
         |  |
         /  \
              """)

        print("Principal Ms. Grandma G: Hello, feisty one!")
        print(f"\n{name}: That is not my name!")
        print("\nPrincipal Ms. Grandma G: I don't care, anyway.")
        print(f"{name}s grade: " + get_grade(last_items))

    else:
        print(f"{name}s attempt has ended.")

    print("Items collected: " + str(last_items) + "/10")
    print("Grade: " + get_grade(last_items))
    print("Games played: " + str(games_played))
    print("Wins: " + str(wins))

    save_results()


load_results()

while True:
    play_game()

    choice = choose([
        "Play again",
        "Quit"
    ])

    if choice == "Quit":
        print("Thanks for playing!")
        break