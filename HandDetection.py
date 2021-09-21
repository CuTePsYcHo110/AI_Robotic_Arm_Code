import cvzone
import cv2

cap= cv.VideoCapture(1)
detector= cvzone.HandDetector(maxHands=1 , detectionCon=0.7)
mySerial= cvzone.SerialObject("COM3",9600,1)
while True:
  success , img = cap.read()
  img = detector.findHands(img)
  lmlist , bbox = detector.findPosition(img)
  if lmlist:
    fingers = detector.fingersUp()
    #print(fingers)
    mySerial.sendData(fingers)
  cv.imshow("image" , img )
  cv.waitKey(1)
