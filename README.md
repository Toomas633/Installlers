# Scripts
- [Install scripts](#install-scripts)
  - [xmrig](#xmrig)
    - [How to install](#how-to-install-xmrig)
    - [Optional config](#optional-xmrig-config)
- [Update scripts](#update-scripts)
  - [Portainer &amp; Portainer agent](#portainer)
    - [Features](#portainer-updater-features)
    - [Download](#download-portainer-updater)
- [General use](#general-use-scripts)
  - [File organizer](#file-organizer)
    - [Default configuration](#default-organizer-configuration)
    - [Features](#organizer-features)
    - [Running](#running-organizer)
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

# General use scripts
- [File organizer](#file-organizer)
    - [Default configuration](#default-organizer-configuration)
    - [Features](#organizer-features)
    - [Running](#running-organizer)

Different automation scripts are found in the main directory.

Such as:

* [File organizer (organizer.py)](#file-organizer)

Running:

* Check dependencies
* Just execute the file as any other python script (`python 'file.py'`)

## File organizer
- [Default configuration](#default-organizer-configuration)
- [Features](#organizer-features)
- [Running](#running-organizer)

General use file organizer for removing all but the wanted file extentions, moving files out of subfolders and deleting empty folders.
Default file is set up for using with Plex for cleaning up torrent downloads (movies and tv shows), but extentions can simply be changed in the python script.
**PS! The file must be placed into the folder in which you want the subfolders to be organized!**

### Default organizer configuration
Organizes the movies and tv directories. placed in the folder that contains them.

```
Dir containing organizer.py
├── movies
│   ├── Movie folder
│   │   ├── movie.mkv or movie.mp4
│   │   ├── other files
│   │   ├── sub.srt (might not excist)
│   │   └── subs (optional some have some don't)
│   │       └── subs.srt
│   └── movies folder 2 and so on
├── tv
│   ├── Show folder
│   │   ├── show.mkv or show.mp4
│   │   ├── other files
│   │   └── subs (optional some have some don't)
│   │       └── subs.srt
│   ├── Show folder
│   │   ├── show episode folder
│   │   │   ├── show.mkv or show.mp4
│   │   │   ├── other files
│   │   │   ├── subs.srt (might not excist)
│   │   │   └── subs (optional some have some don't)
│   │   │       └── subs.srt
│   ├── show season folder
│   │   └── show episode folder
│   │       ├── show.mkv or show.mp4
│   │       ├── subs.srt (might not excist)
│   │       └── subs (optional some have some don't)
│   │           └── subs.srt
│   └── show season folder
│       ├── show.mkv or show.mp4
│       ├── show.mkv or show.mp4
│       ├── subs.srt (might not excist)
│       └── subs (optional some have some don't)
│           └── subs.srt
└── other stuf it wont touch
```

Returns

```
Dir containing organizer.py
├── movies
│   ├── Movie folder
│   │   ├── movie.mkv or movie.mp4
│   │   └── subs.srt (from folder and pre excisting)
│   └── movies folder 2 and so on
├── tv
│   ├── Show folder
│   │   ├── show.mkv or show.mp4
│   │   └── subs.srt (from folder and pre excisting)
│   ├── Show folder
│   │   ├── show episode folder
│   │   │   ├── show.mkv or show.mp4
│   │   │   └── subs.srt (from folder and pre excisting)
│   ├── show season folder
│   │   └── show episode folder
│   │       ├── show.mkv or show.mp4
│   │       └── subs.srt (from folder and pre excisting)
│   └── show season folder
│       ├── show.mkv or show.mp4
│       ├── show.mkv or show.mp4
│       └── subs.srt (from folder and pre excisting)
└── other stuf it wont touch
```

### Organizer features

* Log file in the same dir called organizer.log (time stamp and operation) (editable in code) 
* Removes unwanted files
* Moves certain files out of subfolders
* Deletes empty folders
* Default config for torrenting uses the .!qB extention for not deleting mid download files (check qbittorrent settings for enabling it)

### Running organizer
* Download with `sudo wget https://raw.githubusercontent.com/Toomas633/Scripts/main/organizer.py` and place it into the folder you want it to search through (see example above)
  * Run it in the backround while being in the same folder with `nohup python organizer.py`
  * Or run it always after reboot with cron job by adding `0 * * * * python /'path to folder'/organizer.py` using `sudo crontab -e` and adding it to the end of the file
# Donate

Monero: `8Ajf5M6meNpL9TaHuDRbXjAH31LcQ9ge5BEiwMZjLaoiMDZRxaVy19FgbP4tbUKpKoeq1kqCvjyaTdmCMQGhekWoQ2KgVeV`

Bitcoin: `3NPFV9ivECdSgyCXeNk4h5Gm3q1xiDRnPV`

More options on https://toomas633.com/donate.html
