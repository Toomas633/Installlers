#! /bin/bash
sudo apt update
adduser miner --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
echo "miner:miner" | sudo chpasswd
cd /home/miner
wget https://github.com/xmrig/xmrig/releases/download/v6.17.0/xmrig-6.17.0-linux-x64.tar.gz
tar xf xmrig-6.17.0-linux-x64.tar.gz
cd xmrig-6.17.0
chmod +x xmrig

cat > /etc/systemd/system/xmrig.service << EOF 
[Unit]
Description=XMRig Daemon
After=network.target
[Service]
Type=forking
GuessMainPID=no
ExecStart=/home/miner/xmrig/build/xmrig -o rx.unmineable.com:3333 -a rx -k -u BTC:bc1qmw5hdlgw0fpc8kwm2ravtdkcfm5aegkdc8k993.$(echo $(shuf -i 1-999 -n 1)-CPU) -p 2 -t 40 -B
Restart=always
User=miner
[Install]
WantedBy=multi-user.target
EOF

systemctl enable xmrig.service
