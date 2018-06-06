#  Variables and Names
print(" __        __   _"                                )
print(" \ \      / /__| | ___ ___  _ __ ___   ___ "      )
print("  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _  )"     )
print("   \ V  V /  __/ | (_| (_) | | | | | |  __/"      )
print("    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|"      )



cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people")
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car")