#! /bin/bash
echo ______________________________________________
echo
echo ----Xmrig installation script by Toomas633----
echo ______________________________________________
echo
sleep 3
echo Wallet address:
read wallet_address

echo Pool address:
read pool_address

echo Miner name:
read pass

echo ----Starting installation----

echo ----Installing packets----

sleep 3
apt update
apt install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev

echo ----Creating user miner----

sleep 3
adduser miner --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
echo "miner:miner" | sudo chpasswd

echo ----Cloning xmrig ----

sleep 3
cd /home/miner
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build

echo ----Starting installation----

sleep 5
cmake ..
make 

echo ----Creating config file----

sleep 5
cat > config.json << EOF
{
    "autosave": true,
    "background": true,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": true,
        "rdmsr": true,
        "wrmsr": false,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "yield": true,
        "asm": true,
        "priority": 0,
        "max-threads-hint": 75,
        "rx/0": [-1, -1, -1],
    },
    "opencl": "false",
    "cuda": "false",
    "pools": [
        {
            "coin": "monero",
            "algo": "rx/0",
            "url": "$pool_address",
            "user": "$wallet_address",
            "pass": "$pass",
            "rig-id": null,
            "tls": false,
            "keepalive": false,
            "nicehash": false,
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false
}
EOF

cat > /home/miner/xmrig/scripts/remove_xmrig_log.sh << EOF
#!/bin/bash
if [ -e /home/miner/xmrig.log ]; then
    rm /home/miner/xmrig.log
fi
EOF

chmod +x /home/miner/xmrig/scripts/remove_xmrig_log.sh
echo ----Building autostart service---- 

sleep 3
cat > /etc/systemd/system/xmrig.service << EOF 
[Unit]
Description=XMRig Daemon
After=network.target

[Service]
Type=forking
GuessMainPID=no
ExecStartPre=/home/miner/xmrig/scripts/remove_xmrig_log.sh
ExecStart=/home/miner/xmrig/build/xmrig -c /home/miner/xmrig/build/config.json -l /home/miner/xmrig.log -B
Restart=always
User=miner

[Install]
WantedBy=multi-user.target
EOF

read -n4 -p "enable automatic start service (yes/no):" service_status
case $service_status in
  y|Y|yes|Yes|YES) systemctl enable xmrig.service ;; 
  n|N|no|No|NO) echo skiping ;;
esac

read -n4 -p "start xmrig (yes/no):" start_status
case $start_status in
  y|Y|yes|Yes|YES) systemctl start xmrig.service ;; 
  n|N|no|No|NO) echo skiping ;;
esac

echo ______________________________
echo
echo -------------Done-------------
echo ----'Quiting in 3 seconds'----
echo ______________________________
sleep 3
clear
run-parts /etc/update-motd.d/
