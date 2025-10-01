# Face Recognition App

Une application de reconnaissance faciale en temps réel utilisant Python, OpenCV et la librairie `face_recognition`. Le projet permet de détecter et d'identifier des personnes à partir d'un flux vidéo (webcam) en comparant les visages avec une base d'images connues.

---

## Fonctionnalités

- Détection de visages en temps réel.
- Reconnaissance des visages à partir d'une base d'images (`persons/`).
- Affichage du nom de la personne reconnue et horodatage.
- Gestion des personnes inconnues.
- Détection continue avec mise à jour de la dernière personne vue.

---

## Structure du projet

face_recognition/
│
├─ main.py # Script principal de reconnaissance faciale
├─ requirements.txt # Dépendances du projet
├─ persons/ # Répertoire contenant les images des personnes à reconnaître
└─ venv/ # Environnement virtuel Python


---

## Prérequis

- Python 3.8 ou supérieur (Python 3.13 peut poser problème avec certaines dépendances comme `dlib`)
- Pip installé
- Webcam fonctionnelle

Librairies Python utilisées :

- `numpy`
- `opencv-python`
- `dlib`
- `cmake`
- `face_recognition`

> ⚠️ Si l’installation de `dlib` ou `face_recognition` échoue, il est recommandé d’utiliser Python 3.8, d’installer `cmake` en premier, puis `dlib` avant `face_recognition`.





