from sys import argv

script, input_file = argv

def print_all(f):    #function print_all definition
    print(f.read())    #print the file

def rewind(f):    #funtion declaration
    f.seek(0)    # the method seek() is used to move to a new file position.
                 # In this case the position 0, it means at the beginning of the file.

def print_a_line(line_count, f):    #function print_a_line declaration
    print(line_count, f.readline()) # print the number line_count

current_file = open(input_file) # open the file

print("First let's print the whole file \n")

print_all(current_file) # call the function print_all to print the current_file

print("Now let's rewind, kind of like a tape")

rewind(current_file) # reset the position file to 0 calling the function rewind()

print("\nLet's print three lines: \n")

for current_line in range(1,4):
    print_a_line(current_line, current_file)

#Study Drills
#   1. Write English comments for each line to understand what that line does.
#   2. Each time print_a_line is run, you are passing in a variable current_line . Write out what cur-
#   rent_line is equal to on each function call, and trace how it becomes line_count in print_a_line .
#   3. Find each place a function is used, and check its def to make sure that you are giving it the right
#   arguments.
#   4. Research online what the seek function for file does. Try pydoc file , and see if you can figure
#   it out from there. Then try pydoc file.seek to see what seek does.
#   5. Research the shorthand notation += , and rewrite the script to use += instead.