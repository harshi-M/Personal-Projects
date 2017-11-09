import cv2
import numpy as np
from matplotlib import pyplot as plt

def SecondMaxPeakValueOfHist(x, y):
    peakValue = secondPeakValue = -1
    for i in y:
        print i
    return secondPeakValue
        
#Read the image
img = cv2.imread('malaria_affected1.png',0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255

#apply the mask to image
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with out mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])

# Calculate histogram with mask
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])


#Store the masked image histogram values into a tuple
x, y = hist_mask

#all the graphs display
#Display image
plt.subplot(221), plt.imshow(img, 'gray')
#Display mask
plt.subplot(222), plt.imshow(mask,'gray')
#display image with mask applied
plt.subplot(223), plt.imshow(masked_img, 'gray')

#Diaplay the graph plotted with the pixes and its count using the masked histogram data
plt.subplot(224), plt.plot(hist_mask)
#apply the x limits to the graph
plt.xlim([150,256])
plt.title('Histogram for the blood smear x axis- pixel value and y axis number of pixels')


secondMaxPeakValueOfHist = SecondMaxPeakValueOfHist(x, y)
if secondMaxPeakValueOfHist == -1 :
    print "error"
else:
    print "pixel values of malaria infected cell masked image - " + x[secondMaxPeakValueOfHist]
    print "number of pickels in the mased image - " + y[secondMaxPeakValueOfHist]


plt.show()

