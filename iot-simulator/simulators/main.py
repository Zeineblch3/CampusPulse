
import json
import time
from pathlib import Path
from simulators.mqtt_client import MQTTClient

from simulators.room_simulator import RoomSimulator


# Chemin vers le fichier de configuration
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "rooms.json"


def load_rooms():
    """Charge les salles depuis le fichier JSON."""

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = json.load(file)

    return [
        RoomSimulator(room_config)
        for room_config in config["rooms"]
    ]


def display_room_data(data):
    """Affiche les mesures d'une salle."""

    print(f"\n--- {data['name']} ({data['roomId']}) ---")
    print(f"Température : {data['temperature']} °C")
    print(f"Humidité    : {data['humidity']} %")
    print(f"Présence    : {'Oui' if data['presence'] else 'Non'}")
    print(f"Luminosité  : {data['light']} lux")
    print(f"Éclairage   : {'ON' if data['lighting'] else 'OFF'}")
    print(f"Ventilation : {'ON' if data['ventilation'] else 'OFF'}")
    print(f"Horodatage  : {data['timestamp']}")


def main():
    rooms = load_rooms()

    mqtt_client = MQTTClient()
    mqtt_client.connect()

    print("=" * 45)
    print("       CAMPUSPULSE - SIMULATEUR IOT")
    print("=" * 45)
    print(f"Nombre de salles simulées : {len(rooms)}")
    print("Salles : A102 et A103")
    print("Simulation démarrée. CTRL+C pour arrêter.")

    try:
        while True:
            print("\n" + "=" * 45)
            print("          NOUVELLES MESURES")
            print("=" * 45)

            for room in rooms:
                data = room.generate_data()
                mqtt_client.publish(data)
                display_room_data(data)

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nSimulation arrêtée proprement.")
        mqtt_client.disconnect()


if __name__ == "__main__":
    main()
