Excercice 1 a 3 : 

Suivi les instructions pour installer Docker et verifier la version

PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker --version
Docker version 29.8.0, build 88096ef

et aussi créer le projet local sur IDE et aussi sur Github et faire le lien 



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

- Telecharger l'image officiel Nginx :
    * docker pull nginx

    resultat :
    xS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> 
Using default tag: latest
latest: Pulling from library/nginx
6b37362b3da7: Pull complete 
f1169c633cbc: Pull complete 
2056b40bae09: Pull complete 
46243d3234ed: Pull complete 
f802f27d954b: Pull complete 
3326c3817340: Pull complete 
afa8dec48454: Pull complete 
37d8c7707e42: Download complete 
e40088050cb6: Download complete 
Digest: sha256:abe47724e466aeab9a345d8e46a221c2fa8953c7848bb4a3bd9976a7199f8cf2
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

- Lancer un conteneur Nginx en arriere plan :
    * docker run -d -p 8080:80 --name mon_nginx nginx

    resultat :
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker run -d -p 8080:80 --name mon_nginx nginxAGE IPM\DEVops\TP1> 
22c27548d3d0586f01ed45d5d9d62d9c5e9a4fd293f9adb72ce419124818d622

- Verifier que le conteneur est actif :
    * docker ps

    resultat :
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATEDSTATUS          PORTS                                         NAMES
22c27548d3d0   nginx     "/docker-entrypoint.…"   13 seconds agoUp 12 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp       mon_nginx
696ee41e40cc   tp1-web   "python app.py"          6 days agoUp 4 minutes    0.0.0.0:3500->3500/tcp, [::]:3500->3500/tcp   flask-hello-world
d9be2a951c98   mongo:7   "docker-entrypoint.s…"   6 days agoUp 4 minutes    27017/tcp   

- Ouvrir http://localhost:8080 dans le navigateur
resultat :  page par defaut de Nginx

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
  => [internal] load build definition from Dockerfile          0.1s
 => => transferring dockerfile: 205B                          0.0s
 => [internal] load metadata for docker.io/library/python:3.  1.6s
 => [internal] load .dockerignore                             0.0s
 => => transferring context: 2B                               0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:2f1  1.9s
 => => resolve docker.io/library/python:3.12-slim@sha256:2f1  0.1s
 => => sha256:06ad939ed42b51caafb25b14810875d14e 249B / 249B  0.1s
 => => sha256:b0dc7f87bef15c2536cb182d6c48 12.12MB / 12.12MB  1.0s
 => => sha256:3764a9a7d1e8a98213ab2201a41dbf 1.29MB / 1.29MB  0.6s
 => => extracting sha256:3764a9a7d1e8a98213ab2201a41dbf3da9c  0.2s
 => => extracting sha256:b0dc7f87bef15c2536cb182d6c48b52f90a  0.7s
 => => extracting sha256:06ad939ed42b51caafb25b14810875d14e0  0.0s
 => [internal] load build context                             0.0s
 => => transferring context: 696B                             0.0s
 => [2/5] WORKDIR /app                                        0.1s
 => [3/5] COPY requirements.txt .                             0.1s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt  8.0s
 => [5/5] COPY app.py .                                       0.1s
 => exporting to image                                        3.1s
 => => exporting layers                                       2.2s
 => => exporting manifest sha256:c0ba3739c91036d6bc4d6f3fe2e  0.0s
 => => exporting config sha256:5bec5dbf23b5d451ac8de6d99b959  0.0s
 => => exporting attestation manifest sha256:e23174cfcef0590  0.0s
 => => exporting manifest list sha256:3d8ca873fd91a2bde88dc8  0.0s
 => => naming to docker.io/library/flask-hello-world:latest   0.0s
 => => unpacking to docker.io/library/flask-hello-world:late  0.7s
PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> 

- Lancer le conteneur :
    * docker run -d -p 3500:3500 flask-hello-world

    resultat :
   docker run -d -p 3500:3500 flask-hello-world MIAGE IPM\DEVops\TP1> 
88a7931ac0e4df1a33b4f262c9f0eec15b2b1ba223fd1e1ed010e284219e3425

- Test dans le navigateur sur http://localhost:3500 -> affiche "Hello, World!"


Exercice 6 : Utilisation de docker compose

Objectif : deployer une application plus complexe avec Docker (Flask + MongoDB).

- Modification de app.py pour ajouter une connexion a une bdd MongoDB route /db-check qui fait un ping sur Mongo avec pymongo) -> voir app.py

- Ecriture du docker-compose.yml avec les deux conteneurs (web + mongo) -> voir docker-compose.yml

- Lancer le docker compose :
    * docker compose up -d --build

    resultat :
     => [internal] load local bake definitions                                      0.0s
 => => reading from stdin 537B                                                  0.0s
 => [internal] load build definition from Dockerfile                            0.0s
 => => transferring dockerfile: 205B                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim             0.6s
 => [internal] load .dockerignore                                               0.1s
 => => transferring context: 2B                                                 0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:2f17fc044b579bab302c2  0.1s
 => => resolve docker.io/library/python:3.12-slim@sha256:2f17fc044b579bab302c2  0.1s
 => [internal] load build context                                               0.0s
 => => transferring context: 63B                                                0.0s
 => CACHED [2/5] WORKDIR /app                                                   0.0s
 => CACHED [3/5] COPY requirements.txt .                                        0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt             0.0s
 => CACHED [5/5] COPY app.py .                                                  0.0s
 => exporting to image                                                          0.2s
 => => exporting layers                                                         0.0s
 => => exporting manifest sha256:e17b24202dff53ab08754107f6a7e6e2d3aa1651a16c2  0.0s
 => => exporting config sha256:623d7644791061d9f4c6ad93e602da9ddc3822059123a24  0.0s
 => => exporting attestation manifest sha256:f37cd182815f047c348a7fde40fbf244c  0.0s
 => => exporting manifest list sha256:3c4c93ccd81d1fbdf1442b018fce08d8cb25fffa  0.0s
 => => naming to docker.io/library/tp1-web:latest                               0.0s
 => => unpacking to docker.io/library/tp1-web:latest                            0.0s
 => resolving provenance for metadata file                                      0.0s
[+] up 3/3
 ✔ Image tp1-web               Built                                             1.9s
 ✔ Container mongo             Started                                           0.6s
 ✔ Container flask-hello-world Started   

- Verifier que les deux conteneurs tournent :
    * docker ps

    resultat :
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker ps 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                         NAMES
fdff8cbd89d3   tp1-web   "python app.py"          19 seconds ago   Up 18 seconds   0.0.0.0:3500->3500/tcp, [::]:3500->3500/tcp   flask-hello-world
f2a92d4fee8b   mongo:7   "docker-entrypoint.s…"   19 seconds ago   Up 18 seconds   27017/tcp                                     mongo

- Verifier que la connexion a la bdd s'est bien effectuee en allant sur http://localhost:3500/db-check

    resultat :
Connexion a MongoDB reussie !

- Arreter et supprimer les conteneurs :
    * docker compose down

    resulat : 
    PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> docker compose down
[+] down 3/3
 ✔ Container flask-hello-world Removed                                           0.5s
 ✔ Container mongo             Removed                                           0.4s
 ✔ Network tp1_default         Removed  



à la fin je depose mon travail sur git : 
 - Git init
 - Git remote add origin https://github.com/reda9627/TP-Docker.git
 - git add .
 - PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> git commit -m "depose TP1"
[master (root-commit) 7faa447] depose TP1
 6 files changed, 208 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 Readme.md
 create mode 100644 app.py
 create mode 100644 docker-compose.yml
 create mode 100644 requirements.txt
 create mode 100644 tp_docker.pdf

 - git branch -m main

 - PS C:\Users\moham\Desktop\M2 MIAGE IPM\DEVops\TP1> git push origin main
 
 Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 14 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 210.07 KiB | 7.50 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/reda9627/TP-Docker.git
 + c5cb401...7faa447 main -> main (forced update)







