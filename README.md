\# Mini-projet 1 – Docker



\## 1. Description



Ce projet consiste à développer une application web avec Python Flask et à la conteneuriser avec Docker.



L'application affiche un message personnalisable grâce à une variable d'environnement.



\## 2. Technologies utilisées



\- Python 3.12

\- Flask 3.1.2

\- Docker

\- Docker Hub

\- Git et GitHub



\## 3. Structure du projet



\- `app.py` : application Flask.

\- `requirements.txt` : dépendances Python.

\- `Dockerfile` : instructions de construction de l'image.

\- `.dockerignore` : fichiers exclus du contexte de construction.

\- `.gitignore` : fichiers exclus du dépôt Git.

\- `README.md` : documentation du projet.



\## 4. Construction de l'image Docker



```bash

docker build -t mini-projet-flask:1.0 .

```



\## 5. Lancement du conteneur



```bash

docker run -d --name mini-flask -p 5000:5000 mini-projet-flask:1.0

```



\## 6. Accès à l'application



Ouvrir le navigateur à l'adresse :



http://localhost:5000



\## 7. Configuration avec une variable d'environnement



La variable `APP\_MESSAGE` permet de personnaliser le message affiché par l'application.



Exemple :



```bash

docker run -d --name mini-flask-env -p 5001:5000 -e APP\_MESSAGE="Bonjour depuis Docker !" mini-projet-flask:1.0

```



\## 8. Versions publiées sur Docker Hub



Les versions publiées sont :



\- `1.0`

\- `1.0.0`

\- `1.0.1`

\- `2.0`



\## 9. Télécharger l'image depuis Docker Hub



```bash

docker pull amalmabrouk91/mini-projet-flask:1.0.1

```



\## 10. Liens du projet



\*\*Docker Hub :\*\*



https://hub.docker.com/r/amalmabrouk91/mini-projet-flask



\*\*GitHub :\*\*



https://github.com/amalmuk/mini-projet-docker



