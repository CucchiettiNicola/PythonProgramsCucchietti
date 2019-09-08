people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# Study Drill 4
if not cats < dogs:
    print("The cats are NOT more than dogs.")

if cats >= people or dogs >= people:
    print("Pets are more or equal than people.")

#   Study Drills
#   1. What do you think the if does to the code under it?
#   >  The if struct is used to verify a condition.
#   2. Why does the code under the if need to be indented four spaces?
#   >  Because it's the code that will be runned if the condition is True.
#   3. What happens if it isn’t indented?7
#   >  If the code it is not idented, the code under the if will be always runned, so the
#      if condition becomes useless.
#   4. Can you put other boolean expressions from Exercise 27 in the if-statement ? Try it.
#   5. What happens if you change the initial values for people , cats , and dogs ?
#   >  Outputs could be different.

