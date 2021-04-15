import cv2
import numpy as np
import face_recognition
import os

def FaceRec(tempText):
    
    # ImageFirebase.BringFromFirebase()

    path = r'/Users/admin/VScode/Mini-Project-III-Python/Mini-Module/ResFaceRecog/'
    images = []
    classNames = []
    
    
    def findEncodings(images):

        encodeList = []

        for img in images:

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            encode = face_recognition.face_encodings(img)[0]

            encodeList.append(encode)

        return encodeList

    myList = os.listdir(path)
    print(myList)

    for cls in myList:

        curImg = cv2.imread(f'{path}/{cls}')

        images.append(curImg)

        classNames.append(os.path.splitext(cls)[0])

    print(classNames)
    
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    
    flag = True
    
    while True:
        
        while flag == True:   

            img = face_recognition.load_image_file(path + tempText)

            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)

            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodingsCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodingsCurFrame, facesCurFrame):

                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)

                FaceDist = face_recognition.face_distance(encodeListKnown, encodeFace)

                # print(FaceDist)

                matchIndex = np.argmin(FaceDist)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    flag = False 

                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2),
                            (0, 255, 0), cv2.FILLED)

                    cv2.putText(img, name, (x1 + 6, y2 - 6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                
                    print("Welcome to MITSOE " + name)
                
                else:
                    print("Did not recognise user")
                    
        if flag == False:
            break
    
    return name


# FaceRec('peta.jpg')