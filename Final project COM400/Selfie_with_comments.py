#These are the imports 
import numpy as np
import cv2

#These are data that is being checked to the video
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haaracascade_face.xml')
eye_cascade = cv2.CascadeClassifier('haaracascade_glasses.xml')

#set video input
cap = cv2.VideoCapture(0)

#asks user for files name
photo_name = input('What would you like the photos image to be? \n(File Extension: .PNG)\nFilename:')
photo_taken = False
idle = False

#continously going until the letter 'C'
while cv2.waitKey(30) & 0xff != ord('c'):
    #reading a frame from the video
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # using the face detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    x = 0
    # does this for every face seen
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        roi_text = frame[y:y+h, x:x+w]
        # using the eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray)
        num_eyes = 0

        #loops through all visible eyes
        for (ex,ey,ew,eh) in eyes:
            num_eyes = num_eyes + 1
            # wherever there is an eye, put a square around it and label
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,'eye',(ex+x,ey+y), font, .4, (30,30,30), 2, cv2.LINE_AA) 
        instructions = ''
        # based on the visible amount of eyes the text above the face is changed
        if num_eyes < 2:
            instructions = 'OPEN Both EYES'
        elif num_eyes >=2:
            instructions = 'PHOTO READY, SMILE'
            if not photo_taken and not idle:
                # lets the user know that a picture will be saved
                print('Photo:'+photo_name+'.png Saved check directory to get photo')
                photo_taken = True
                # picture saved
                ret,frame = cap.read()

                # picture is saved
                cv2.imwrite(photo_name+'.png',frame)
                
                #checks to see if the user wants to take another picture then prompts the user for an input to restart the process
                response = input('Would you like to take another picture?(Y/N/I => set idle)')
                if response == 'Y':
                    img = input("what is the name of the next image?")
                    photo_name = img
                    photo_taken = False
                elif response == 'N':
                    cap.release()
                    cv2.destroyAllWindows()
                    exit() 
                elif response == 'I':
                    idle = True
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                cap.release()
                cv2.destroyAllWindows() 
        #based on the status, the instructions are on top of the detected face   
        cv2.putText(frame,instructions,(x-20,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,30,0), 2, cv2.LINE_AA) 

    # shows the live video from the frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

# gracefully ends the program
cap.release()
cv2.destroyAllWindows()

# Example of the data from the .XML file for detection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# <maxWeakCount>9</maxWeakCount>
#       <stageThreshold>-5.0425500869750977e+00</stageThreshold>
#       <weakClassifiers>
#         <_>
#           <internalNodes>
#             0 -1 0 -3.1511999666690826e-02</internalNodes>
#           <leafValues>
#             2.0875380039215088e+00 -2.2172100543975830e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 1 1.2396000325679779e-02</internalNodes>
#           <leafValues>
#             -1.8633940219879150e+00 1.3272049427032471e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 2 2.1927999332547188e-02</internalNodes>
#           <leafValues>
#             -1.5105249881744385e+00 1.0625729560852051e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 3 5.7529998011887074e-03</internalNodes>
#           <leafValues>
#             -8.7463897466659546e-01 1.1760339736938477e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 4 1.5014000236988068e-02</internalNodes>
#           <leafValues>
#             -7.7945697307586670e-01 1.2608419656753540e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 5 9.9371001124382019e-02</internalNodes>
#           <leafValues>
#             5.5751299858093262e-01 -1.8743000030517578e+00</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 6 2.7340000960975885e-03</internalNodes>
#           <leafValues>
#             -1.6911929845809937e+00 4.4009700417518616e-01</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 7 -1.8859000876545906e-02</internalNodes>
#           <leafValues>
#             -1.4769539833068848e+00 4.4350099563598633e-01</leafValues></_>
#         <_>
#           <internalNodes>
#             0 -1 8 5.9739998541772366e-03</internalNodes>
#           <leafValues>
#             -8.5909199714660645e-01 8.5255599021911621e-01</leafValues></_></weakClassifiers></_>