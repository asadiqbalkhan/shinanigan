def superbikes(yamaha_r1, kawasaki_h2):
	print("You have %d bikes in the garage" % (bikes_count))
	print("You have %d spare tires available" % (spare_tires))
	print("According to todays weather riding the %s is better" % (select_bike))

	print("We can just give the functions numbers directly")

	superbikes(20,40,'Yamaha')

	print("OR, we can use variables from our script")

	bikes_available = 10
	tires_available = 20
	superbikes(bikes_available,tires_available)

	print("We can even do math inside too:")
	superbikes(10 + 20, 40 + 2)

	print("And we can combine the two, variables and math:")
	superbikes(bikes_available + 100, tires_available + 200)

	