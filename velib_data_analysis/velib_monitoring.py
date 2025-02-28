import os
import requests
import csv
import time
import logging
from datetime import datetime
import signal

# chemin absolu du répertoire du script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Remonte d'un niveau depuis scripts/

# Configuration
URL = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel%40parisdata&rows=2000"
FILENAME = os.path.join(BASE_DIR, "data", "velib_data.csv")
LOG_FILENAME = os.path.join(BASE_DIR, "logs", "velib_monitoring.log")
os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
SLEEP_INTERVAL = 120  # secondes


# Configurer le logging
os.makedirs(os.path.dirname(LOG_FILENAME), exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(LOG_FILENAME, mode='w', encoding='utf-8'),
    logging.StreamHandler()
])

# Variable globale pour contrôler l'arrêt du script
running = True

def signal_handler(sig, frame):
    global running
    logging.info("Signal reçu, arrêt du script...")
    running = False

# Enregistrer le gestionnaire de signal pour intercepter Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def fetch_data():
    """Récupère les données en temps réel de l'API Vélib."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()["records"]
    except requests.RequestException as e:
        logging.error(f"Erreur lors de la récupération des données: {e}")
        return []

def save_to_csv(data):
    """Sauvegarde les données dans un fichier CSV."""
    try:
        # Vérifiez si le répertoire existe, sinon créez-le
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
        
        with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id_station", "nom_station", "velos_mecaniques", "velos_electriques", "capacite", "longitude", "latitude", "timestamp"])
            for record in data:
                fields = record["fields"]
                writer.writerow([
                    fields.get("stationcode", "N/A"),
                    fields.get("name", "N/A"),
                    fields.get("mechanical", 0),
                    fields.get("ebike", 0),
                    fields.get("capacity", 0),
                    fields.get("coordonnees_geo", [0, 0])[1],
                    fields.get("coordonnees_geo", [0, 0])[0],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ])
    except IOError as e:
        logging.error(f"Erreur lors de la sauvegarde des données: {e}")

def monitor_station():
    """Surveille une station sans vélos et envoie une alerte quand un vélo devient disponible."""
    logging.info("Début de la surveillance des stations...")
    empty_stations = set()
    
    while running:
        data = fetch_data()
        for record in data:
            fields = record["fields"]
            station_id = fields.get("stationcode", "N/A")
            nb_velos = fields.get("mechanical", 0) + fields.get("ebike", 0)
            
            if nb_velos == 0:
                empty_stations.add(station_id)
            elif station_id in empty_stations:
                logging.info(f"🚴 Un vélo est maintenant disponible à la station {station_id} !")
                empty_stations.remove(station_id)
        
        time.sleep(SLEEP_INTERVAL)  # Attente avant la prochaine requête

def main():
    """Point d'entrée pour `velib-monitor`."""
    data = fetch_data()
    save_to_csv(data)
    monitor_station()

if __name__ == "__main__":
    main()
