import urllib
#import hashlib
import time
import sys
from PIL import ImageChops #the library that contains useful functions for comparing images
from PIL import Image
import os

location=raw_input('Enter the location to save the images (e.g. C:\img\ ):')
no_of_images=int(input('How many images do you need?'))
prev_filename=''
#filename=''
#imestamp=''

def retrieve_image():
	print "\nretrieving image.."
	global filename
	filename=time.strftime("%Y%m%d-%H%M%S")
	urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',location+filename+'.jpg')
	global prev_filename
	prev_filename=filename+'.jpg'

def compare_images(im1,im2):
	img1=Image.open(im1) #open the images
	img2=Image.open(im2)
	return ImageChops.difference(img1, img2).getbbox() is None

time_it_takes=no_of_images*15*60 #check every 15 minutes

if no_of_images==0:
	sys.exit(0)
elif no_of_images==1:
	retrieve_image()
elif no_of_images>1:
	print "This will take some time as the script will check for new images every 15 minutes. Do not close the program." 

	retrieve_image()
	count=1
	while(True):
		if count!=no_of_images:
			for n in range(time_it_takes,0,-1):
				sys.stdout.write('Next snap in %d seconds' %n)   #print in the same line
				sys.stdout.flush()
				time.sleep(1)
			retrieve_image()
			duplicate=compare_images(location+filename+'.jpg',location+prev_filename) #compare the two images
			if duplicate:
			#delete the file and continue to next iteration
				os.remove(location+prev_filename)
				count-=1
				continue
			else:
			#rename the tmp file with timestamp
				os.rename(location+prev_filename,location+filename+'.jpg')
				count+=1


print 'done.'
