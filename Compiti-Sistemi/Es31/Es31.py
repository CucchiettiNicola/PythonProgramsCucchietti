print("""You enter a dark room with two doors.
Do you go trough door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Screm at the bear.")

    bear = input()

    if bear == "1":
        print("The bear eats your face off. Good job!")
    if bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

        print("You realize that you are in a dark forest.")
        print("You can see a path in the darkness.")
        print("What do you do?")
        print("1. Follow the path.")
        print("2. Go back to the dark room.")

        darkForest = input("> ")

        if darkForest == "1":
            print("You don't see anything because it's very dark.")
            print("You fall into a ravine.")
            print("You are dead.")
        elif darkForest == "2":
            print("The door is closed and you can't open it.")
        else:
            print("You decide to stop a minute to think what to do.")

        if int(darkForest) >= 2:
            print("GRRRRRRRR!")
            print("The bear is coming back with other bears.")
            print("The bears are angry with you.")
            print("The bears eat you.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

    print("Gs!dhsg j£hu sdj$sdi sjh/su kk^k ahge.")
    print("*Nothing have sense here. I think it's a Game Over?*")

else:
    print("You stumble around and fall on a knife and die. Good Job!")

print("""
 _______  _______  __   __  _______    _______  __   __  _______  ______   
|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  
|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  
|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ 
|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |
|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |
|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_||_||_||_|""")

#   Study Drill
#   1. Make new parts of the game and change what decisions people can make. Expand the game out
#   as much as you can before it gets ridiculous
#   2. Write a completely new game. Maybe you don’t like this one, so make your own. This is your
#   computer; do what you want.