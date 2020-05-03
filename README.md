# Centaure
Le fichier deep_learning_train_and_evaluate.ipynb permet d'entraîner un réseau de neurones à partir d'une banque d'images d'un circuit et de vérifier ce réseau à partir d'un modèle de Keras. 


Le fichier deep_learning_use.py n'est pas foncionnel et n'a pas été testé
Il s'agit du squelette de l'architecture du code pour réaliser le deep learning sur le centaure

Voici les étapes à suivre :

 - Importer le réseau correspondant au circuit demandé
 - Récupérer les images renvoyées par la kinect
 - Les convertir avec la fonction shape en une matrice
 - Réaliser les prédictions
 - Lier cette prédiction à une direction
 - Envoyer cette direction à la kinect
