#this one is like your scripts whith argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

def checklist():
    print("1. Did you start your function definition with def?")
    print("2. Does your function name have only characers and _(underscore) characters?")
    print("3. Did you put an open parenthesis ( right after the function name?")
    print("4. Did you put your arguments after the parenthesis ( separated by commas?")
    print("5. Did you make each argument unique (meaning no duplicated names)?")
    print("6. Did you put a close parenthesis and a colon ): after the arguments?")
    print("7. Did you indent all lines of code you want in the function four spaces? No more, no less.")
    print("8. Did you ”end” your function by going back to writing with no indent (dedenting we call it)?")

print_two("Rick", "Morty")
print_two_again("Rick", "Morty")
print_one("First!")
print_none()
print("Checklist:")
checklist()

# Study Drills
#   Create a function checklist for later exercises. Write these checks on an index card and keep it by you
#   while you complete the rest of these exercises or until you feel you do not need the index card anymore: