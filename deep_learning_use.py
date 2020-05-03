#Importation des bibliothèques nécessaires

from serial import *
import os
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

#Récupération du ciruit correspond à la destination demandée

dossier='/content/'+ 'circuit1.h5'

# Création du modèle à partir du fichier importé
new_model = tf.keras.models.load_model(dossier)

#Récupération des images de la kinect converties avec OpenCV

def shape(photo): # Convertir une image en tableau
  image=[]
  for i in range (0,1): #Récupérer la première photo du dossier 
    dossier_img="/img_kinect/"+photo[i]
    img= load_img(dossier_img) #Charge l'image au format PIL
    img = img_to_array(img) #Convertit l'image PIL en un tableau numpy
    image.append(img) #On ajoute l'image à notre liste
    os.remove(dossier_img) #On supprime l'image du dossier
  return image
    
photo = listdir("dos") #dos correspond au dossier dans lequel seront stockées les images


# Prédictions

def predic(new_model,tab_img):
    
    probability_model = tf.keras.Sequential([new_model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict(tab_img)

# Dictionnaire liant les prédictions aux directions
pred_direction={0:"gauche",31:"diagonale gauche",63:"tout droit", 95:"diagonale droite", 127:"droite"}


while (1):

    tab_img = shape(photo)
    tab_img=np.array(tab_img)
    tab_img=tab_img/255.0
    predic(new_model, tab_img)
# Evaluer les prédictions

    direction = pred_direction[np.argmax(predictions)] #ou prediction de [0] pour être sûr d'avoir une seule direction

# Envoyer la direction à la kinect

    f = open("direction.txt","w")
    f.write(direction)
    f.close()
            

    





