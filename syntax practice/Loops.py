# Loops and Lists
# Program to find the sum of all numbers stored in a list

# List of numbers 
# A list is simply an Array

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# # variable to store the sum
# sum = 0
# # iterate over the list
# for val in numbers:
# 	sum += val
# # Output: the sum is 48
# print("The sum is ",sum)


the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print("This is count %d" % (number))

# same as above
for fruit in fruits:
	print("The fruit of type: %s" % (fruit))

# Also we can go through mixed lists too
# notice we have to use %r since we don't know what's in iterate
for i in change:
	print("I got %r" % (i))

# We can also build lists, first start with an empty one 
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print("Adding %d to the list." % (i))
	elements.append(i)

# Now we can print them out too
for i in elements:
	print("Element was: %d" % (i))
	