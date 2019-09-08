the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartiers']

# this first kind of for-loop goes trough a list

for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go trough mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counte
for i in range(0,6):
    print(f"Adding {i} to the list")
    # append is a function that lists understand
    elements.append(i)

# this print out element values
print("Elements -> {}".format(elements))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

#   Study Drills
#   1. Take a look at how you used range. Look up the range function to understand it.
#   >  range() function create a list of numbers from the first to the second.
#      For example: range(2, 5) -> [2,3,4]  (5 it's not included)
#   2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly
#      to elements ?
#   >  elements = range(0,6)
#   3. Find the Python documentation on lists and read about them. What other operations can you do
#      to lists besides append ?
#   >  clear, copy, extend, index, insert, pop, remove, reverse, sort
