# Scripts

- [Install scripts](#install-scripts)
  - [xmrig](#xmrig)
- [Minecraft scripts](#minecraft-scripts)
  - [Server services](#server-services)
- [Update scripts](#update-scripts)
  - [Portainer &amp; Portainer agent](#portainer)
- [Donate](#donate)

Some ease of life scrypts that I felt like I could not find or use frequently. Only meant for running on debian systems (Ubuntu a.s.o). **Python scripts should also work on windows but it is not guaranteed!**
Install and upgrade scripts have no need for a specific folder, but there also is no cleanup, all donwloaded files will have to be removed manualy. **Other scripts might need a certain working directory (placement) so read the topic!**

# Install scripts

- [xmrig](#xmrig)
  - [How to install](#how-to-install-xmrig)
  - [Optional config](#optional-xmrig-config)

Different automated install scripts are found in the install folder.

Such as:

* [xmrig (xmrig.sh)](#xmrig)

## xmrig

- [How to install](#how-to-install-xmrig)
- [Optional config](#optional-xmrig-config)

Automatic cloning, building and configuring of xmrig for Debian systems (PiOSx64,Ubuntu (server)).

See log file with `cat /home/miner/xmrig.log`

* Asks for your wallet address and mining pool URL with port (for example `gulf.moneroocean.stream:10128`) and device/miner name
* Creates a specific "miner" user so your home folder won't be cluttered
* Autoconfigures for startup and control as service (xmrig.service)

### How to install xmrig

* Download the file with `sudo wget https://raw.githubusercontent.com/Toomas633/Scripts/main/install/xmrig.sh`
* Allow running with `sudo chmod a+x xmrig.sh`
* Run `sudo ./xmrig.sh`, fill in the 3 questions, and wait

### Optional xmrig config

* Add `"rx/0": [-1, -1, -1],` to `/home/miner/xmrig/build/config.json` under `cpu:` configuration to control cpu usage (each -1 represents a thread)
* Set `max-threads-hint:` to use up only given % on startup
* Change `priority: 0` value (0-5) to run on the backround and only use up free recources (default) or allocate more importance to it

# Minecraft scripts

- [Server background services](#server-services)

## Server services

Automatically start and/or stop systemd services running on your server. Script outputs will be logged to `mc-background.log` file in the same folder as the python script.
Requirements:

* Python 3
* mcstatus python package `sudo pip install mcstatus`

Installing:

* Download the mc-background.py file from the minecraft folder or via `wget https://raw.githubusercontent.com/Toomas633/Scripts/main/minecraft/mc-background.py`
* Change the variables (python file) `server_address` to your minecraft server address and `service_name` to the service you want to control
* Allow running `sudo chmod a+x mc-background.py`
  * Run it in the backround while being in the same folder with `nohup python3 mc-background.py`
  * Or run it every minute with cron job by adding `* * * * * python3 /<path_to_script>/mc-background.py` using `sudo crontab -e` and adding it to the end of the file

# Update scripts

- [Portainer &amp; Portainer agent](#portainer)
  - [Features](#portainer-updater-features)
  - [Download](#download-portainer-updater)

Different automated update scripts are found in the update folder.

Such as:

* [Portainer (update_portainer.sh) &amp; Portainer agent (update_portainer_agent.sh)](#portainer)

Running:

* Allow execution via `sudo chmod a+x 'file'`
* Run as any script and answer any questions (`./'file'`)

## Portainer

- [Features](#portainer-updater-features)
- [Download](#download-portainer-updater)

Automated update script to update Portainer to latest version. Optionally can also update portainer agent within the same script or use the update_portainer_agent.sh to only update the agent if only portainer agent is used on the server.

### Portainer updater features

* Main update_portainer.sh will ask upon completion if the portainer agent should also be updated or not (downloads update_portainer_agent and runs it)

### Download Portainer updater

* update_portainer.sh `sudo wget https://raw.githubusercontent.com/Toomas633/Scripts/main/update/portainer/update_portainer.sh`
* update_portainer_agent.sh `sudo wget https://raw.githubusercontent.com/Toomas633/Scripts/main/update/portainer/update_portainer_agent.sh`

# Donate

[toomas633.com/donate](https://toomas633.com/donate/)
