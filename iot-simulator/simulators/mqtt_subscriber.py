
import json
import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 8883
TOPIC = "campuspulse/rooms/+/data"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Subscriber connecté au broker MQTT !")
        client.subscribe(TOPIC)
        print("Abonné au topic :", TOPIC)


def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode("utf-8"))

        print("\n========== MESSAGE REÇU ==========")
        print("Topic :", message.topic)
        print("Salle :", data["roomId"])
        print("Température :", data["temperature"], "°C")
        print("Humidité :", data["humidity"], "%")
        print("Présence :", data["presence"])
        print("Luminosité :", data["light"], "lux")
        print("Éclairage :", data["lighting"])
        print("Ventilation :", data["ventilation"])
        print("==================================")

    except (json.JSONDecodeError, KeyError) as e:
        print("Erreur de traitement du message :", e)

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="campuspulse_subscriber_test"
)

client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

print("Connexion au broker...")

client.connect(BROKER, PORT, 60)

client.loop_forever()
