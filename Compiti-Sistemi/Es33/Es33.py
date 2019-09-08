def while_loop(loops, inc):
    i = 0
    numbers = []
    while i < loops:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + inc
        print("Numbers now", numbers)
        print(f"At the bottom i is {i}")
    return numbers

loops = 10     # this variable replaces 6
inc = 3
numbers = while_loop(loops, inc)

print("The numbers: ")

for num in numbers:
    print(num)

#   Study Drills
#   1. Convert this while-loop to a function that you can call, and replace 6 in the test ( i < 6 ) with a
#      variable.
#   2. Use this function to rewrite the script to try different numbers.
#   3. Add another variable to the function arguments that you can pass in that lets you change the +
#      1 on line 8 so you can change how much it increments by.
#   4. Rewrite the script again to use this function to see what effect that has.
#   5. Write it to use for-loops and range . Do you need the incrementor in the middle anymore? What
#      happens if you do not get rid of it?
#   >  The incrementor isn't necessary in a for loop because it is managed by Python.

