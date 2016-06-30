import os
import sys
import cv2
import getopt

def usage():
	print "Image Distinguish(white and black)"
	print "-a          :Takes all of pictures from the same directory with the project to distinguish."
	print "-n [picture]:Takes the picture selected to distinguish.\n"
	print "example:"
	print "python ImageDistinguish.py -a"
	print "python ImageDistinguish.py -n xxx.jpg"
	sys.exit(0)

def main(picName,allPicture):
	if allPicture:
		picName = [file for file in os.listdir('.') if ".jpg" in file or ".png" in file]

	with open('result.txt','w') as f:
		for pic in picName:
			try:
				img = cv2.imread(pic)
				white = 0.0
				black = 0.0
				allPixels = img.shape[0] * img.shape[1]
				for height in xrange(img.shape[0]):
					for width in xrange(img.shape[1]):
						(b, g, r) = img[height, width]
						if b < 50 and g < 50 and r < 50:
							img[height,width] = (0,255,0)
							black+=1
						elif b > 240 and g > 240 and r > 240:
							img[height,width] = (255,0,0)
							white+=1

				print >>f,"image: %s" % str(pic)
				print >>f,"[r>240,g>240,b>240]White:%.2f %% " % (float(white)/float(allPixels)*100)
				print >>f,"[r< 50,g< 50,b< 50]Black:%.2f %% " % (float(black)/float(allPixels)*100)
				outputFileName = "%s-Distinguished.%s" % (str(pic).split('.')[0],str(pic).split('.')[-1])
				cv2.imwrite(outputFileName,img)
				print >>f,"View the %s.(white->blue,black->green)\n" % outputFileName
				print "%s is finished." % str(pic)
			except:
				print "There are some problems with %s." % pic

if not len(sys.argv[1:]):
	usage()

try:
	opts, args = getopt.getopt(sys.argv[1:],"an:",["all","name"])
except getopt.GetoptError as err:
	print str(err)

allPicture = False
picName = []

for o,v in opts:
	if o in ("-a","--all"):
		allPicture = True
	elif o in ("-n","--name"):
		picName.append(v)
	else:
		pass

main(picName,allPicture)