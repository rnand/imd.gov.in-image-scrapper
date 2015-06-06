import urllib
import hashlib
import time
import sys

location=raw_input('Enter the location to save the images:')
no_of_images=int(input('How many images do you need?'))
if no_of_images>1:
	print "This will take a while.. do not close the program.."

if no_of_images==0:
	sys.exit(0)

print 'retrieving first image..'
filename=time.strftime("%Y%m%d-%H%M%S")
urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',location+filename+'.jpg')
prev_filename=filename+'.jpg'
#mdhash=hashlib.md5(filename+'.jpg').hexdigest()
#print mdhash
for n in range(2,no_of_images,1):
	print 'waiting for 1 minute..'
	time.sleep(60)
	print 'retrieving image ',n


#hashlib.md5()
#urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',"F:\img\img1.jpg")
