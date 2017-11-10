'''  Image Scaling using Spline Interpolation   : Aadish Goel '''
  
from scipy.misc import toimage
from skimage.transform import rescale
import cv2

#old = cv2.VideoCapture(0).read()[1]    #For Capturing Realtime photo from webcam  
old = cv2.imread("picture.jpg")         #For Loading Picture From Working Directory 

#Default order 1  Can be changed by giving optional argument "order" to rescale funtion
# eg.  rescale(image=old, scale=5, order=1) Order Can take value from 0-5

new = rescale(old, 5)                   # 5 is the scale factor                               

#For printing the size of pixel grid
#print(old.shape)
#print(new.shape)

old = toimage(old)
new = toimage(new)

old.show()
new.show()
