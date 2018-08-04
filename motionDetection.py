import cv2

def differenceImgs(I0, I1, I2):
  diff1 = cv2.absdiff(I2, I1)
  diff2 = cv2.absdiff(I1, I0)
  return cv2.bitwise_and(diff1, diff2)

camera = cv2.VideoCapture(0)

windowName = "Simple Motion Detection"
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

# First will read all three images

I_minus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
I = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)
I_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

while True:
  cv2.imshow( windowName, differenceImgs(I_minus, I, I_plus) )

  # Read next image
  I_minus = I
  I = I_plus
  I_plus = cv2.cvtColor(camera.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)
  
  if key == 27: #use ESC key to stop window 
    cv2.destroyWindow(winName)
    break
