import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('cc1.jpg')
print('This image is:', type(image), 
      ' with dimensions:', image.shape)

image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
lower_blue = np.array([0,0,200])  
upper_blue = np.array([250,250,255])
mask = cv2.inRange(image_copy, lower_blue, upper_blue)
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)
background_image = cv2.imread('bg2.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
crop_background = background_image[0:452, 0:678]

try:
  crop_background[mask == 0] = [0,0,0]
except:pass
complete_image = masked_image + crop_background
plt.imshow(complete_image)
plt.axis("off")
plt.savefig('fc.png', bbox_inches='tight')
