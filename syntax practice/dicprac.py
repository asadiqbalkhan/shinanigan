#  Practicing Dictionary concept

riders = {'Valentino':' World Champion 7 times',
		  'Marquez':' World Champion 3 times',
		  'Lorenzo':' World Champion 3 times',
		  'Pedrosa':' Never won'
			}

# print(riders['Valentino'])

# Use a for loop
# k = key for example and v is the value of the dict
for k, v in riders.items():
	print(k + v)