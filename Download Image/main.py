# Author: Asad Iqbal
# Purpose of this program: Download images from any website using python

# Use the random library
import random
# Import urllib.request to process the image url from the web
import urllib.request

# Function to download the web image
def download_web_image(url):
	name = random.randrange(1,1000)
	# specify the image type
	full_name = str(name) + ".jpeg"
	urllib.request.urlretrieve(url, full_name)
# Source of the image in the parenthesis 
download_web_image("https://www.asphaltandrubber.com/wp-content/uploads/2012/10/2013-BMW-S1000RR-HP4-119.jpg")
