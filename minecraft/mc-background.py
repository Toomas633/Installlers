import mcstatus
import time
import datetime
import os
import subprocess
import logging

path = os.path.dirname(os.path.abspath(__file__))
log_path = path + '/mc-background.log'
logging.basicConfig(filename=log_path, level=logging.DEBUG, format='[%(asctime)s] - %(levelname)s: %(message)s')

def clear_log(log_file_path):
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=30)

    with open(log_file_path, "r") as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if line.startswith("[")]
    filtered_lines = [line for line in filtered_lines if datetime.datetime.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M:%S,%f') >= cutoff_date]

    with open(log_file_path, "w") as file:
        file.writelines(filtered_lines)


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
        clear_log(log_path)
    except Exception as e:
        logging.exception(e)