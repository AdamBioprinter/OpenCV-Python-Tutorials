import cv2
import numpy as np

Str = " BoYa, registered Left button double click"
Str2 = "Entered draw circle function"

WinName = "Image"

# mouse callback function
def draw_circle(event, x, y, flags, param):
  # Problem! This computer does not sense a left button double click
  # instead the if statement below has been modified to sense a left button down
  # (1 click)
  if event == cv2.EVENT_LBUTTONDOWN:
    cv2.circle(img, (x,y), 100, (255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.int8)
cv2.namedWindow(WinName)
cv2.setMouseCallback(WinName,draw_circle, 0)

while(1):
  cv2.imshow(WinName,img)
  if cv2.waitKey(20) & 0xFF == 27:
    break
cv2.destroyAllWindows()
