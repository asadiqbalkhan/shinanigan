#  List of commands

# close -- Closes the file. 
# read -- Reads the contents in your file
# readline -- Reads just one line of a text file
# trancate -- Empties the file. Watch out if you care about a file
# write('stuff') -- Writes "stuffs" to the file

# Lets use some of this to make a simple little text editor

from sys import argv

script, filename = argv

print("We're going to erase %r" % (filename))
print("If you don't want that, hit control-c")
print("If you do want that, hit return ")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()