# assign values to variables
people = 40
cars = 40
trucks = 15

if cars > people:
    """If cars variable is greater than people variable"""
    print("We should take the cars.")
elif cars < people:
    """If cars variable is lower than people variable"""
    print("We should not take the cars.")
else:
    """If cars variable is equal to people variable"""
    print("We can't decide.")

if trucks > cars:
    """If trucks value is greater than cars value"""
    print("That's too many trucks.")
elif trucks < cars:
    """If trucks value is lower than cars value"""
    print("Maybe we could take the trucks.")
else:
    """If trucks value is equal to cars value"""
    print("We still can't decide.")

if people > trucks:
    """If people number is greater than trucks number"""
    print("Allright, let's just take the trucks.")
else:
    """If there people number is lower or equal to trucks number"""
    print("Fine, let's stay home then.")

# Strudy Drill 3
if trucks + cars >= people:
    print("We can take trucks and cars.")
else:
    print("We must stay home.")

#   Study Drills
#   1. Try to guess what elif and else are doing.
#   >  Elif is used to check another condition if the first condition isn't True.
#      Else is used to run a piece of code if previous conditions are not True.
#   2. Change the numbers of cars , people , and trucks , and then trace through each if-statement
#      to see what will be printed.
#   >  people = 60; cars = 40; trucks = 70
#      We should not take the cars.
#      That's too many trucks.
#      Fine, let's stay home then.
#   3. Try some more complex boolean expressions like cars > people or trucks < cars .
#   4. Above each line write an English description of what the line does.
