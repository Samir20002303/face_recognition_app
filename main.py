import time
from datetime import datetime
import numpy as np
import cv2
import face_recognition
import os

path = 'persons' # Chemin vers le répertoire contenant les images des personnes à reconnaître

# tableau pour stocker les images et les noms des personnes
images = []
classNames = []

# Liste des noms de fichiers d'images dans le répertoire
personsList = os.listdir(path)

for cl in personsList:
    curPersonn = cv2.imread(f'{path}/{cl}')
    images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodeings(image):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodeings(images)
print('Encoding Complete.')

cap = cv2.VideoCapture(0)

recognized_person = None
delay_time = 5
last_seen_time = time.time()


# Boucle principale pour la capture et la reconnaissance des visages en temps réel

while True:
    success, img = cap.read()

    if not success:
        print("La capture vidéo a échoué.")
        break

    # Redimensionnement et converti en RGB
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Détection et encodage des caracteristique faciales
    faceCurentFrame = face_recognition.face_locations(imgS)
    encodeCurentFrame = face_recognition.face_encodings(imgS, faceCurentFrame)

    for faceLoc in faceCurentFrame:
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    face_detected = False


    #puis on compare les caracteristique faciale des visage detectés avec celle deja connu
    for encodeface, faceLoc in zip(encodeCurentFrame, faceCurentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeface)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
        matchIndex = np.argmin(faceDis)

        name = "Inconnu"
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            current_time = datetime.now().strftime("%H:%M:%S")

            if name != recognized_person:
                recognized_person = name
                recognized_time = time.time()
                print(f'{name} : {current_time}')

            last_seen_time = time.time()
            face_detected = True

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    if not face_detected and (time.time() - last_seen_time) >= delay_time:
        recognized_person = None

    cv2.imshow('Face Recogntion', img)
    cv2.waitKey(1)