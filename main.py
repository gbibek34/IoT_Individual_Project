# Importing required libraries
import cv2
import time
import os
import sys
# Local Files
import authentication
import device_control

# Camera object to find OpenCV
cap = cv2.VideoCapture(0)

# QR code detection Method
detector = cv2.QRCodeDetector()

def main():
# Loop to keep the scanning realtime
    while True:
        
        # Reads image that appears in camera
        _, img = cap.read()
        
        # Fetching data by reading the QR Code
        data, blue_box, _ = detector.detectAndDecode(img)
        
        # Shows the qrcode and data in the scanner
        if(blue_box is not None):
            for i in range(len(blue_box)):
                cv2.line(img, tuple(blue_box[i][0]), 
                        tuple(blue_box[(i+1) % len(blue_box)][0]), color=(255, 0, 0), thickness=2)
            
            # Using the data to authenticate the doorlock 
            if data:
                # print("data found: ", data, date, current_time)
                authenticated = authentication.authentication(data)
                #Authenticating the user
                if authenticated is not None:
                    print(f"Welcome {authenticated}")
                    device_control.device_control(True)
                    authentication.record(data)
                    break
                if authenticated is None:
                    print("Authorization Failed")
                    device_control.device_control(False)
                    break
                
        # Live feed of the scanning process
        cv2.imshow("QR Scanner", img)
        
        # For stopping the code if required press 's'
        if(cv2.waitKey(1) == ord("s")):
            sys.exit()
        
    # Closing all the processes after code stops
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    os.execv(sys.executable, [sys.executable] + sys.argv)



