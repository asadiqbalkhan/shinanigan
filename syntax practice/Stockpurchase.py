SELL_PRICE_POINT = 54.2
BUY_PRICE_POINT = 28.2

def ask_stock_value():

	print("What is the current stock value?")
	input("> ",value)

def make_devision():
	if value <= BUY_PRICE_POINT:
		print("I suggest you to buy more of this stock.")
	elif value >= SELL_PRICE_POINT:
		print("I suggest you to sell this stock.")
	elif value == SELL_PRICE_POINT:
		print("Lets wait and see what the market is doing.")
	else:
		print("Sorry, I cannot provide any advice at this time.")


