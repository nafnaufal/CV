import cv2 as cv
  
cam_port = 0
cam = cv.VideoCapture(cam_port)
  
result, image = cam.read()
  
if result:
  
    cv.imshow("Test", image)
  
    # cv.imwrite("test.png", image)
  
    cv.waitKey(0)
    cv.destroyWindow("Test")
  
else:
    print("Error!")
