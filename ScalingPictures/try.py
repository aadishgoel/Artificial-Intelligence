'''  Image Scaling using Spline Interpolation   : Aadish Goel '''
  
from scipy.misc import toimage
from skimage.transform import rescale
import cv2

#old = cv2.VideoCapture(0).read()[1]    
old = cv2.imread("picture.jpg")         

new = rescale(old, 5)                                              

print(old.shape)
print(new.shape)

old = toimage(old)
new = toimage(new)

old.show()
new.show()
