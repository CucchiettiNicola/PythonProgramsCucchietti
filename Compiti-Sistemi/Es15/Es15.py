from sys import argv

script, filename = argv # assign script and filename from arguments (unpack the arguments)

txt = open(filename) # open the file filename and creates a file obejct called txt

print(f"Here's your file {filename}")   # print the name of the file
print(txt.read())   # the method read() return a string of whatever is written in the file and then print it 

txt.close() # close the file

print("Type the filename again")
file_again = input(">")

txt_again = open(file_again) # try to open the new file called file_again and creates a file obejct called txt_again

print(txt_again.read()) # the method read() return a string of whatever is written in the file and then print it 

txt_again.close() # cloese the file

# Study Drills
# 1. Above each line, write out in English what that line does.
# 2. If you are not sure, ask someone for help or search online. Many times searching for ”python3.6
#    THING” will find answers to what that THING does in Python. Try searching for ”python3.6 open.”
# 3. I used the word ”commands” here, but commands are also called ”functions” and ”methods.”
#    You will learn about functions and methods later in the book.
# 4. Get rid of the lines 10-15 where you use input and run the script again.
# 5. Use only input and try the script that way. Why is one way of getting the filename better than
#    another? > Because it's possible tell the user what to enter, the filename in this case.
# 6. Start python3.6 to start the python3.6 shell, and use open from the prompt just like in this pro-
#    gram. Notice how you can open files and run read on them from within python3.6? 
# 7. Have your script also call close()