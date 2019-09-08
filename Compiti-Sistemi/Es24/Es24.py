print("Let's practice everything.")
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# """ is used for multiline strings
poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) # apply format() string method

# it's just like awith an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point) # formula is a tuple


# This is an easy way to apply a list to a format string.
# Formula is a tuple, alternatively separate values using commas.
print("We'd have {} beans, {} jars, and {} crates".format(*formula))

#Study Drills
#   1. Make sure to do your checks: read it backward, read it out loud, and put comments above con-
#   fusing parts.
#   2. Break the file on purpose, then run it to see what kinds of errors you get. Make sure you can fix
#   it.
#   > SyntaxError: EOL while scanning string literal