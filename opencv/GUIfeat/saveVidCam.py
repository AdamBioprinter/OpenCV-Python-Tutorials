import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

# The video writer object take the following input arguments:
# cv2.VideoWriter( output filename (say output.avi), fourcc video codec I420 for quicktime ( I think), fps, frame size, isColor)
out = cv2.VideoWriter()

succes = out.open('output.mp4v', fourcc, 15.0, (1280,720),True)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # Flip frame in vertical direction
    frame = cv2.flip(frame,0)

    # write the flipped frame
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  else:
    break

# release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


