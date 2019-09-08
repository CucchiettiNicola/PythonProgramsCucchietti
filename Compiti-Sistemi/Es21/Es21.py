def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLIYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100, 2)

# A puzzle for the extra credit, type it anyway.
print("Here is a puzzle")

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")

#   Study Drills:
#   1. If you aren’t really sure what return does, try writing a few of your own functions and have them
#   return some values. You can return anything that you can put to the right of an = .
#   2. At the end of the script is a puzzle. I’m taking the return value of one function and using it as the
#   argument of another function. I’m( doing this in a chain so that I’m kind of creating a formula using
#   the functions. It looks really weird, but if you run the script, you can see the results. What you
#   should do is try to figure out the normal formula that would recreate this same set of operations.
#   >   what = age + (height - (weight * (iq/2)))
#   3. Once you have the formula worked out for the puzzle, get in there and see what happens when
#   you modify the parts of the functions. Try to change it on purpose to make another value.
#   4. Do the inverse. Write a simple formula and use the functions in the same way to calculate it.

# Study Drill 1
def odd_or_even(n):
    if(n%2):
        return "Odd"
    else:
        return "Even"

print("\nHere some output to test odd_or_even function.\n")

# to test my function
for n in range(1,10):
    print(f"{n} is ", odd_or_even(n))

#Study Drill 3
print("\nHere's study drill 3")
study3 = add(age, multiply(weight, subtract(height, divide(iq, 2)))) 
print("\nHere's what we get when we switch the multiple and divide functions:", study3)

#study Drill 4 (study4 = age * (iq-weight) / height + 2)
print("\nHere's study drill 4")
study4 = divide( multiply(age, subtract(iq,weight) ), add(height,2))
print("\nHere's the result: ", study4)