Excercice 1 a 3 : 

Suivi les instructions pour installer Docker et verifier la version

PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker --version
Docker version 29.8.0, build 88096ef

et aussi créer le projet local sur IDE et aussi sur Github et faire le lien 

Git remote add origin https://github.com/reda9627/TP-Docker.git

Exercice 3: 
- voir les image avec docker :
    * Docker images 
- puis Telecharger image hello-world Puis run : 
    * docker pull hello-world 
    * docker run hello-world 
- listez les conteneurs & conteneurs actifs :
    * docker ps -a 
    * docker ps

    Resulat de run :
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

- Essayer de supprimer le conteneur: 
    * docker rm  

    resultat : 
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker rm 0ebcc8d44599
0ebcc8d44599


    * Docker rm container-Id

    PS : docker run hello-run ne crée pas un conteneur donc pas suppression possible ou bien 


Exercice 4 : Creation d'un serveur web avec Docker

- Telecharger l'image officielle Nginx :
    * docker pull nginx

    resultat :
    (coller ici le resultat du docker pull)

- Lancer un conteneur Nginx en arriere plan :
    * docker run -d -p 8080:80 --name mon_nginx nginx

    resultat :
    (coller ici le resultat)

- Verifier que le conteneur est actif :
    * docker ps

    resultat :
    (coller ici le resultat du docker ps)

- Ouvrir http://localhost:8080 dans le navigateur -> page par defaut de Nginx.

- Arreter le conteneur :
    * docker stop mon_nginx

- Supprimer le conteneur :
    * docker rm mon_nginx


Exercice 5 : Deploiement d'une application Python Flask

Objectif : creer et lancer une appli web simple avec Flask a l'aide de Docker.

- Creation du fichier app.py avec une appli Flask minimale (hello world) -> voir app.py

- Ecriture du Dockerfile pour construire l'image de l'appli -> voir Dockerfile

- Build de l'image :
    * docker build -t flask-hello-world .

    resultat :
    (coller ici le resultat du build)

- Lancer le conteneur :
    * docker run -d -p 3500:3500 flask-hello-world

    resultat :
    (coller ici le resultat)

- Test dans le navigateur sur http://localhost:3500 -> affiche "Hello, World!"


Exercice 6 : Utilisation de docker compose

Objectif : deployer une application plus complexe avec Docker (Flask + MongoDB).

- Modification de app.py pour ajouter une connexion a une bdd MongoDB (route /db-check qui fait un ping sur Mongo avec pymongo) -> voir app.py

- Ecriture du docker-compose.yml avec les deux conteneurs (web + mongo) -> voir docker-compose.yml

- Lancer le docker compose :
    * docker compose up -d --build

    resultat :
    (coller ici le resultat)

- Verifier que les deux conteneurs tournent :
    * docker ps

    resultat :
    (coller ici le resultat du docker ps)

- Verifier que la connexion a la bdd s'est bien effectuee en allant sur http://localhost:3500/db-check

    resultat :
    (coller ici le message affiche par la page, ex: "Connexion a MongoDB reussie !")

- Arreter et supprimer les conteneurs :
    * docker compose down









