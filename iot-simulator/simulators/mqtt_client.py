
import json
import uuid
import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 8883


class MQTTClient:

    def __init__(self):
        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2,
            client_id=f"campuspulse_{uuid.uuid4().hex[:12]}"
        )

        # Activer TLS
        self.client.tls_set()

        self.client.on_connect = self.on_connect

    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print("Connexion au broker MQTT réussie !")
        else:
            print("Erreur de connexion MQTT :", reason_code)

    def connect(self):
        self.client.connect(BROKER, PORT, 60)
        self.client.loop_start()

    def publish(self, data):
        topic = f"campuspulse/rooms/{data['roomId']}/data"

        payload = json.dumps(data, ensure_ascii=False)

        result = self.client.publish(topic, payload)

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Message envoyé vers : {topic}")
        else:
            print("Erreur lors de l'envoi MQTT")

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()
