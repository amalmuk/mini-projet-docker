

\# Mini-projet 1 – Docker



\## Description

Application web développée avec Python Flask et conteneurisée avec Docker.



\## Technologies utilisées

\- Python 3.12

\- Flask 3.1.2

\- Docker

\- Docker Hub



\## Structure du projet

\- app.py : application Flask

\- requirements.txt : dépendances Python

\- Dockerfile : instructions de construction

\- .dockerignore : fichiers exclus de la construction

\- README.md : documentation



\## Construction de l'image

```bash

docker build -t mini-projet-flask:1.0 .

```



\## Lancement du conteneur

```bash

docker run -d --name mini-flask -p 5000:5000 mini-projet-flask:1.0

```



\## Accès à l'application

http://localhost:5000



\## Configuration

La variable d'environnement APP\_MESSAGE permet de personnaliser le message affiché.



\## Image Docker Hub

amalmabrouk91/mini-projet-flask



\## Versions publiées

\- 1.0

\- 2.0



