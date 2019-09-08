from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")

# we could these two on one line, how? 
# > Yes, but we have problem closing the file.
# indata = open(from_file, "rb").read()

in_file = open(from_file, "rb")
indata = in_file.read()

out_file = open(to_file, "wb")
out_file.write(indata)

print("Allright, all done!")

out_file.close()
in_file.close()

# Study Drills
#   1. This script is really annoying. There’s no need to ask you before doing the copy, and it prints too
#   much out to the screen. Try to make the script more friendly to use by removing features.
#   2. See how short you can make the script. I could make this one line long.
#    > (Thanks to StackOverflow) 
#    from sys import argv; script, from_file, to_file = argv; open(to_file, 'wb').write(open(from_file, "rb").read())

#   3. Notice at the end of the What You Should See I used something called cat ? It’s an old command
#   that ”con*cat*enates” files together, but mostly it’s just an easy way to print a file to the screen.
#   Type man cat to read about it.
#   4. Find out why you had to write out_file.close() in the code.
#   > It is necessary to create it (or save it if already exists) and let access it from other programs.
#   5. Go read up on Python’s import statement, and start python3.6 to try it out. Try importing some
#   things and see if you can get it right. It’s alright if you do not.