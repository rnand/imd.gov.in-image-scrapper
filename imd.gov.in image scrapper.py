import urllib
#import hashlib
import time
import sys
from PIL import ImageChops
from PIL import Image
import os

location=raw_input('Enter the location to save the images:')
no_of_images=int(input('How many images do you need?'))
prev_filename=''
filename=''
timestamp=''

def retrieve_image():
	print 'retrieving image..'
	global filename
	filename=time.strftime("%Y%m%d-%H%M%S")
	urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',location+filename+'.jpg')
	global prev_filename
	prev_filename=filename+'.jpg'

def compare_images(im1,im2):
	img1=Image.open(im1)
	img2=Image.open(im2)
	return ImageChops.difference(img1, img2).getbbox() is None

time_it_takes=no_of_images*1*2

if no_of_images==0:
	sys.exit(0)
elif no_of_images==1:
	retrieve_image()
elif no_of_images>1:
	print "This will take some time.. do not close the program.." 

	retrieve_image()
	for i in range(1,no_of_images+1,1):
		for n in range(time_it_takes,0,-1):
			sys.stdout.write('Next snap in %d seconds' %n)
			sys.stdout.flush()
			time.sleep(1)
		retrieve_image()
		duplicate=compare_images(location+filename+'.jpg',location+prev_filename)
		if duplicate:
		#delete the file and continue to next iteration
			os.remove(location+prev_filename)
			continue
		else:
		#rename the tmp file with timestamp
			os.rename(location+prev_filename,location+filename+'.jpg')


print 'done.'
