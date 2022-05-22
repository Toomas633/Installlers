# Installers
- [Installers](#installers)
  * [Xmrig install script:](#xmrig-install-script)
    + [To install:](#to-install)
    + [Optional:](#optional)
  * [Donate:](#donate)

## Xmrig install script:
Automatic cloning, building and configuring of xmrig for PiOSx64 or Ubuntu (server).
* Asks for your wallet address and mingin pool url with port *(for example `gulf.moneroocean.stream:10128`)* and device/miner name.
* Creates a specific *"miner"* user so your home folder won't be cluttered.
* Autoconfigures for startup and control as service *(xmrig.service)*.
### How to install:
* Download the file with `sudo wget https://raw.githubusercontent.com/Toomas633/configs/main/installers/xmrig.sh`
* Allow running with `sudo chmod a+x xmrig.sh`
* Run `sudo ./xmrig.sh`, fill in the 3 questions, and wait.
### Optional:
* Add `"rx/0": [-1, -1, -1],` to `/home/miner/xmrig/build/config.json` under cpu: configuration to control cpu usage (each -1 represents a thread).
## Donate:
Monero: `8Ajf5M6meNpL9TaHuDRbXjAH31LcQ9ge5BEiwMZjLaoiMDZRxaVy19FgbP4tbUKpKoeq1kqCvjyaTdmCMQGhekWoQ2KgVeV`

Bitcoin: `3NPFV9ivECdSgyCXeNk4h5Gm3q1xiDRnPV`

More options on https://toomas633.com/donate.html
