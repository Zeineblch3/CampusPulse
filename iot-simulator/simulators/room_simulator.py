
import random
from datetime import datetime


class RoomSimulator:
    def __init__(self, room_config):
        self.room_id = room_config["id"]
        self.name = room_config["name"]
        self.building = room_config["building"]

        self.temperature = room_config["temperature"]
        self.humidity = room_config["humidity"]
        self.presence = room_config["presence"]
        self.light = room_config["light"]

        # États initiaux des actionneurs
        self.lighting = False
        self.ventilation = False

    def generate_data(self):
        """Génère de nouvelles mesures pour la salle."""

        # Variation de température
        self.temperature += random.uniform(-0.5, 0.5)
        self.temperature = max(15, min(40, self.temperature))
        self.temperature = round(self.temperature, 1)

        # Variation d'humidité
        self.humidity += random.uniform(-1, 1)
        self.humidity = max(20, min(90, self.humidity))
        self.humidity = round(self.humidity, 1)

        # La présence peut changer occasionnellement
        if random.random() < 0.10:
            self.presence = not self.presence

        # Variation de luminosité
        self.light += random.randint(-30, 30)
        self.light = max(0, min(1000, self.light))

        # Application des règles automatiques
        self.apply_automation_rules()

        return {
            "roomId": self.room_id,
            "name": self.name,
            "building": self.building,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "presence": self.presence,
            "light": self.light,
            "lighting": self.lighting,
            "ventilation": self.ventilation,
            "timestamp": datetime.now().isoformat(timespec="seconds")
        }

    def apply_automation_rules(self):
        """Contrôle automatiquement l'éclairage et la ventilation."""

        # Allumer si une personne est présente et qu'il fait sombre
        self.lighting = self.presence and self.light < 400

        # Activer la ventilation si la température dépasse 28 °C
        self.ventilation = self.temperature > 28
