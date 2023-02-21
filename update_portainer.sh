#!/bin/bash
echo Updating Portainer CE
sudo docker stop portainer
sudo docker rm portainer
sudo docker pull portainer/portainer-ce:latest
sudo docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

sudo wget https://raw.githubusercontent.com/Toomas633/Installers/main/update_portainer_agent
sudo chmod a+x 
