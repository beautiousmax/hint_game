import random

#This is HINT. Like "CLUE", but not copyright infringing.
#Here we have a list of options for a murder.
Char = ["Mrs. Scarlet", "Col. Mustard", "Ms. White", "Mr. Green", "Rebecca Black", "Blue Man Group"]
Weapon = ["Gun", "Candle Stick", "Lead Pipe", "Antifreeze", "Wrench", "Rope", "Arson"]
Rooms = ["Library", "Kitchen", "Dining Room", "Garage", "Office", "Make-out Shed", "Auxiliary Basement"]

#This Dictionary is going randomly select from the options to guess at.
Murder = {"person" : '', "killingthingy" : '', "place": ''}

#Here we populate the dict with the murder facts.
Murder["person"] = random.choice(Char)
Murder["killingthingy"] = random.choice(Weapon)
Murder["place"] = random.choice(Rooms)


print "Isn't this a lovely party? Well, somebody is dead now, let's figure out who."
print
print "Your guests are: " + ", ".join(Char)
print
print "The weapons on hand are: " + ", ".join(Weapon)
print
print "Your weird house has: " + ", ".join(Rooms)
print
print "So, there you have it. Start guessing."
print "Be careful! If you take too long to figure it out, the murderer will get nervous and kill you too!"
print
print

#random number of chances you get to guess:
hints_left = random.randint(25, 36)

#The idea is that after a set of guessing, the number of guesses left counts down.
#The guesses get checked against the murder dict.
#If any guess is wrong, give a hint for a wrong guess.
#i.e. who = Mrs. Scarlet "but Mrs. Scarlet was with me the whole time!"
#When all guesses are right, game won.
#When no guesses are left, game over. Kinda like hangman?? but a little more sinister?


def ask_me_anything(lives):
    correctness = False
    who = raw_input("Who did it? ")
    what = raw_input("With what? ")
    where = raw_input("Where? ")

    while lives > 0:
        wrongers = []
        if who != Murder['person']:
            wrongers.append(who)
        if what != Murder['killingthingy']:
            wrongers.append(what)
        if where != Murder['place']:
            wrongers.append(where)
        if len(wrongers) == 0:
            print "YOU WIN!"
            correctness = True
            lives = 0
        else:
            print str(random.choice(wrongers)) + " isn't right!"
            print
            lives -= 1
            ask_me_anything(hints_left)
    if correctness is False:
        print "You died. " + Murder["person"] + " killed you with " + Murder["killingthingy"] + " in the " + Murder["place"] + "."

ask_me_anything(hints_left)
