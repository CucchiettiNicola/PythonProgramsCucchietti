from sys import argv

script, first, second, third = argv

print(f"The lenght of argv is {len(argv)}\n")

#Study Drills
# 1. Python 3 does not accept fewer arguments 
#    (ValueError: not enough values to unpack)
# 2. /

# 3. Input
name = input("Your name: ")
age = input("Your Age: ")

print(f"\nYour name is {name} and you are {age} y/o\n")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
