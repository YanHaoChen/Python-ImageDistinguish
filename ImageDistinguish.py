import cv2
imageName = "XXX.jpg"
img = cv2.imread(imageName)

white = 0.0
black = 0.0
allPixels = img.shape[0] * img.shape[1]
for height in xrange(img.shape[0]):
	for width in xrange(img.shape[1]):
		(b,g,r)=img[height,width]
		if b < 50 and g < 50 and r <50:
			img[height,width]=(0,255,0)
			black+=1
		elif b > 240 and g >240 and r > 240:
			img[height,width]=(255,0,0)
			white+=1

print imageName
print "All:%d" % allPixels
print "[r>240,g>240,b>240]White:%.2f %% " % (float(white)/float(allPixels)*100)
print "[r< 50,g< 50,b< 50]Black:%.2f %% " % (float(black)/float(allPixels)*100)
print "view Distinguished.jpg(white->blue,black->green)"

outputFileName = "%s-Distinguished.jpg" % imageName

cv2.imwrite(outputFileName,img)
