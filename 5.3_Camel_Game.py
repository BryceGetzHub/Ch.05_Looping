'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done = False

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_from_natives = -20
drinks_left = 7
print()
print("Ride on your camel accross the desert while being chased by the natives.")
print("You must choose to drink, move forward, or stop as you travel along.")
print()

while not done:
    print("A. Drink from your canteen.   B. Ahead moderate speed.    C. Ahead full speed.    D. Stop for the night.    E. Status check.    Q. Quit.")

    choice = input("A, B, C, D, E, or Q?: ")

    oasis = random.randint(1, 5)

    if oasis == 1:
        print("You have found an Oasis!")
        drinks_left = 7
        camel_tiredness = 0
        thirst = 0

    if choice.lower() == "q": #Quitting code
        done = True
    elif choice.lower() == "e": #Status Check
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", drinks_left)
        print("The natives are", distance_from_natives, "miles behind you")

    elif choice.lower() == "d": #Stop for the night
        camel_tiredness = 0
        print("Your camel is happy")
        distance_from_natives += random.randint(7, 15)

    elif choice.lower() == "c": #Fullspeed
        miles_traveled += random.randint(10, 21)
        print("You have traveled", miles_traveled, "miles.")
        thirst = thirst + 1
        camel_tiredness += random.randint(1, 4)
        distance_from_natives += random.randint(7, 15)

    elif choice.lower() == "b": #moderate speed
        miles_traveled += random.randint(5, 13)
        print("You have traveled", miles_traveled, "miles.")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + 1
        distance_from_natives += random.randint(7, 15)

    elif choice.lower() == "a": #drink water
        if drinks_left > 0:
            drinks_left = drinks_left - 1
        if drinks_left < 0:
            print("No more water!!")

    if thirst == (4, 5): #if you are thirsty
        print("You are thirsty!")
    elif thirst == 6: #die of thirst
        print("You died of thirst")
        done = True

    if camel_tiredness == (4, 5, 6): #tired camel
        print("Your camel is tired")

    if camel_tiredness > 6:
        print("Your camel is dead")
        done = True

    if distance_from_natives == 0:
        print("The natives cought you!")
        done = True

    if distance_from_natives < -1:
        print("The natives are getting close!")

    if miles_traveled > 199:
        print("You've Won!")




















