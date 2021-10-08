# LITReview

Openclassroom projet 11

Ce projet est une application web à but pédagogique à exécuter localement.
Cette application permets de gérer un système de competitions et de reservation de place.
le but du projet est la création de différent test.

### Installation et exécution de l'application

1.  Cloner ce dépôt de code à l'aide de la commande  `$ git clone https://github.com/GuillaumeRobin10/ocp11.git`
2.  Rendez-vous dans le dossier ocp10 avec la commande `$ cd ocp11`
3.  Créer un environnement virtuel pour le projet avec  `$ python -m venv env`  sous Windows ou  `$ python3 -m venv env`  sous MacOS ou Linux.
4.  Activez l'environnement virtuel avec  `$ env\Scripts\activate`  sous Windows ou  `$ source env/bin/activate`  sous MacOS ou Linux.
5.  Installez les dépendances du projet avec la commande  `$ pip install -r requirements.txt`
6.  Pour lancer l'application lancez les commandes:
  - `$ export FLASK_APP="server.py"`
  - `$ flask run`


## Utilisation et documentation

Pour lancer les test utilisez la commande `$ pytest`
Pour lancer le rapport locust lancez le serveur puis la commande `$ locust -f locust/locust_files.py`
