import mcstatus
import time
import os
import subprocess
import logging

path = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=path + '/mc-background.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

def get_player_count(server_address):
    try:
        server = mcstatus.JavaServer.lookup(server_address)
        status = server.status()
        player_count = status.players.online
        return player_count
    except Exception as e:
        logging.exception(e)
        return None

def start_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "start", service_name], check=True)
    except subprocess.CalledProcessError:
        logging.error(f"Failed to start {service_name}")

def stop_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "stop", service_name], check=True)
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
    server_address = "ip:port or domain"
    service_name = "example.service"
    try:
        player_count = get_player_count(server_address)
        logging.info(f"Players online: {player_count}")
        if player_count > 0:
            if is_service_running(service_name):
                stop_service(service_name)
                logging.info(f"Stopped {service_name}")
        else:
            if is_service_running(service_name) == False:
                start_service(service_name)
                logging.info(f"Started {service_name}")
    except Exception as e:
        logging.exception(e)