Pour pourvoir run le projet, voici les etapes à suuivre:

1- Intsaller python 3.12.*

2- Installer le module venv de python

    python -m pip install venv

3- Créer un environnement dédié au projet

	Python -m venv .env
 
4- Activer l’env

	source .env/bin/active	#pour linux

	.\env\Script\activate.bat 	#pour windows
 
5- Installer les modules du requierement.txt dans l’env

  Python -m pip install -r requierement.txt
 
6- Run le projet

  	Python manage.py makemigrations
  
  	Python manege.py migrate
  
  	Python manege.py runserver localhost :8000
  
7 – Ainsi vous pouvez accéder à l’interface web dans le navigateur.

	http://localhost:8000
	
