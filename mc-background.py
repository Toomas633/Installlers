import mcstatus
import time
import subprocess
import logging

def get_player_count(server_address):
    try:
        server = mcstatus.JavaServer.lookup(f"{server_address}")
        status = server.status()
        player_count = status.players.online
        return player_count
    except Exception as e:
        logging.exception(e)
        return None
    
def start_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "start", service_name], check=True)
        print(f"{service_name} started successfully.")
    except subprocess.CalledProcessError:
        logging.error(f"Failed to start {service_name}")

def stop_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "stop", service_name], check=True)
        print(f"{service_name} stopped successfully.")
    except subprocess.CalledProcessError:
        logging.error(f"Failed to stop {service_name}")

def is_service_running(service_name):
    try:
        result = subprocess.run(["sudo", "systemctl", "is-active", service_name], capture_output=True, text=True)
        return result.stdout.strip() == "active"
    except subprocess.CalledProcessError as e:
        logging.exception(e)
        return False

if __name__ == "__main__":
    server_address = "vanilla.toomas633.com"
    service_name = "xmrig.service"
    logging.basicConfig('organizer.log', level=logging.INFO, format='%(asctime)s %(message)s')

    while True:
        player_count = get_player_count(server_address)
        logging.info(f"Players online: {player_count}")
        if player_count is not None:
            if is_service_running(service_name) == "active":
                stop_service(service_name)
                logging.info(f"Stopped {service_name}")
        else:
            if is_service_running(service_name) == False:
                start_service(service_name)
                logging.info(f"Started {service_name}")
        time.sleep(60)