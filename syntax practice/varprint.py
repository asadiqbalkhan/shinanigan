# More Variables and Printing
print(" __        __   _"                                )
print(" \ \      / /__| | ___ ___  _ __ ___   ___ "      )
print("  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _  )"     )
print("   \ V  V /  __/ | (_| (_) | | | | | |  __/"      )
print("    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|"      )


my_name = 'Asad Iqbal'
my_age  = 23
my_height = 75 
my_weight = 170
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print("Lets talk about %s" % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair." %(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee" % my_teeth)

# this line is tricky, try to get it exactly right

print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight
	, my_age + my_height + my_weight))