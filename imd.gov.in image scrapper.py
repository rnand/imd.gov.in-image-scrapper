import urllib
import hashlib
import time
import sys

location=raw_input('Enter the location to save the images:')
no_of_images=int(input('How many images do you need?'))

time_it_takes=no_of_images*30*60
if no_of_images>1:
	print "This will more than %d seconds.. do not close the program.." %time_it_takes

if no_of_images==0:
	sys.exit(0)

print 'retrieving first image..'
filename=time.strftime("%Y%m%d-%H%M%S")
urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',location+filename+'.jpg')
prev_filename=filename+'.jpg'
#mdhash=hashlib.md5(filename+'.jpg').hexdigest()
#print mdhash
for n in range(time_it_takes,0,-1):
	sys.stdout.write('Next snap in %d seconds' %n)
	sys.stdout.flush()
	time.sleep(1)
	print 'retrieving image ',n

print 'done.'
#hashlib.md5()
#urllib.urlretrieve('http://www.imd.gov.in/section/satmet/img/sector-ir.jpg',"F:\img\img1.jpg")
