import cv2  #OpenCV library, which is used for image processing

import matplotlib.pyplot as plt #importing matplotlib

image_path = cv2.imread('MRI_image.jpg')#reads an image file

# find frequency of pixels in range 0-255

histr = cv2.calcHist([image_path],[0],None,[256],[0,256])#calcHist function computes the histogram of the image.


''' [image_path]: The image to analyze (wrapped in a list).
·  [0]: The index of the channel to analyze. In this case, 0 refers to the first channel (typically the grayscale channel for single-channel images).
·  None: No mask is applied to the image.
·  [256]: The number of bins for the histogram (256 for pixel values ranging from 0 to 255).
·  [0, 256]: The range of pixel values.   '''

# show the plotting graph of an image

plt.plot(histr)# plots the histogram data calculated
plt.show()   #displays the plot in a window