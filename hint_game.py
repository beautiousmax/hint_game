import random

#This is HINT. Like "CLUE", but not copyright infringing.
#Here we have a list of options for a murder.
Char = ["Mrs. Scarlet", "Col. Mustard", "Ms. White",
        "Mr. Green", "Rebecca Black", "Blue Man Group"]

Weapon = ["Gun", "Candle Stick", "Lead Pipe",
          "Antifreeze", "Wrench", "Rope", "Arson"]

Rooms = ["Library", "Kitchen", "Dining Room", "Garage",
         "Office", "Make-out Shed", "Auxiliary Basement"]

#This Dictionary is going randomly select from the options to guess at.
Murder = {"person": random.choice(Char),
          "killingthingy": random.choice(Weapon),
          "place": random.choice(Rooms)}

#Here we populate the dict with the murder facts.

print("""
 Isn't this a lovely party? Well, somebody is dead now, let's figure out who.

 Your guests are: {0}

 The weapons on hand are: {1}

 Your weird house has: {2}

 So, there you have it. Start guessing.
 Be careful! If you take too long to figure it out,\
the murderer will get nervous and kill you too!
""".format(", ".join(Char), ", ".join(Weapon), ", ".join(Rooms)))


#random number of chances you get to guess:
hints_left = random.randint(25, 36)

#The idea is that after a set of guessing the number of guesses left decreases.
#The guesses get checked against the murder dict.
#If any guess is wrong, give a hint for a wrong guess.
#i.e. who = Mrs. Scarlet "but Mrs. Scarlet was with me the whole time!"
#When all guesses are right, game won.
#When no guesses are left, game over.
#Kinda like hangman?? but a little more sinister?


def ask_me_anything():
    who = raw_input("Who did it? ")
    what = raw_input("With what? ")
    where = raw_input("Where? ")
    return who, what, where


def run_game(lives):
    while lives > 0:
        wrongers = []
        who, what, where = ask_me_anything()
        if who != Murder['person']:
            wrongers.append(who)
        if what != Murder['killingthingy']:
            wrongers.append(what)
        if where != Murder['place']:
            wrongers.append(where)
        if len(wrongers) == 0:
            print("YOU WIN!")
            return
        else:
            print (str(random.choice(wrongers)) + " isn't right!\n")
            lives -= 1
    "You died. \
    {0} killed you with {1} in the {2}.".format(Murder["person"],
                                                Murder["killingthingy"],
                                                Murder["place"])

run_game(hints_left)
