# CampusPulse – Smart Classroom IoT Monitoring

## Créez une cpoie du Lien Wokwi : https://wokwi.com/projects/481309611325101057


## 1. Présentation

CampusPulse est un système IoT de surveillance intelligente des salles de classe.

Il permet de collecter les données environnementales et de surveiller automatiquement les équipements de chaque salle.

Le système utilise :
- ESP32 simulé avec Wokwi.
- Python pour simuler plusieurs salles.
- MQTT pour la communication entre les salles et le système central.
- HiveMQ comme broker MQTT.

## 2. Architecture

Le projet comporte actuellement trois salles :

| Salle | Source | Description |
|---|---|---|
| A101 | ESP32 + Wokwi | Simulation matérielle |
| A102 | Python | Simulation logicielle |
| A103 | Python | Simulation logicielle |

### Capteurs et actionneurs

**Salle A101 – ESP32**
- DHT22 : température et humidité.
- PIR : détection de présence.
- LDR : mesure de luminosité.
- LED : simulation de l'éclairage.
- LED : simulation de la ventilation.

**Salles A102 et A103 – Python**
- Température simulée.
- Humidité simulée.
- Présence simulée.
- Luminosité simulée.
- Éclairage et ventilation simulés.

## 3. Technologies utilisées

- Python 3
- ESP32 / Arduino C++
- Wokwi
- MQTT
- HiveMQ
- Paho MQTT
- DHTesp
- PubSubClient
- WiFiClientSecure

## 4. Configuration MQTT

Broker : `broker.hivemq.com`

Port : `8883` (TLS)

Protocole : MQTT over TLS.

Les topics utilisés sont :

```text
campuspulse/rooms/A101/data
campuspulse/rooms/A102/data
campuspulse/rooms/A103/data
```

Chaque salle publie ses données au format JSON toutes les 5 secondes.

Exemple :

```json
{
  "room": "A102",
  "temperature": 21.1,
  "humidity": 50.2,
  "presence": true,
  "luminosity": 241,
  "lighting": true,
  "ventilation": false
}
```

## 5. Installation du simulateur Python

### Prérequis

- Installer Python 3.
- Installer Git (si le projet est récupéré depuis GitHub).
- Avoir une connexion Internet.

### Étape 1 – Récupérer le projet

Si le projet est sur GitHub :

```powershell
git clone URL_DU_PROJET
```

Sinon, télécharger et extraire le dossier CampusPulse.

### Étape 2 – Accéder au simulateur

```powershell
cd CampusPulse
cd iot-simulator
```

### Étape 3 – Créer un environnement virtuel

```powershell
python -m venv .venv
```

### Étape 4 – Activer l'environnement

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Puis relancer :

```powershell
.\.venv\Scripts\Activate.ps1
```

### Étape 5 – Installer les dépendances

```powershell
python -m pip install --upgrade pip
```

```powershell
pip install -r requirements.txt
```

Dépendance MQTT utilisée :

```text
paho-mqtt==2.1.0
```

### Étape 6 – Lancer la simulation

Depuis le dossier `iot-simulator` :
Simulatanément :

Sur un terminal_1 :
```powershell_1
python -m simulators.main
```
Sur un terminal_2:
```powershell_2
python -m simulators.mqtt_subscriber
```

Résultat attendu :

```text
=============================================
       CAMPUSPULSE - SIMULATEUR IOT
=============================================

Nombre de salles simulées : 2
Salles : A102 et A103

Simulation démarrée. CTRL+C pour arrêter.
```

Les données sont générées et publiées automatiquement toutes les 5 secondes.

Pour arrêter le programme :

```text
CTRL + C
```

## 6. Lancer la simulation ESP32 sur Wokwi

1. Ouvrir le lien du projet Wokwi CampusPulse.
2. Ouvrir le code ESP32.
3. Cliquer sur Start Simulation.
4. Vérifier les messages dans le Serial Monitor.
5. Vérifier la publication MQTT sur le topic :

```text
campuspulse/rooms/A101/data
```

Configuration Wi-Fi :

```cpp
const char* ssid = "Wokwi-GUEST";
```

Configuration MQTT :
- Broker : `broker.hivemq.com`
- Port : `8883`
- Connexion sécurisée TLS.

Le programme utilise les bibliothèques DHTesp, PubSubClient et WiFiClientSecure.

## 7. Vérification

Les messages MQTT doivent être publiés sur les trois topics :

```text
campuspulse/rooms/A101/data
campuspulse/rooms/A102/data
campuspulse/rooms/A103/data
```

Exemple de résultat attendu :

```text
========== MESSAGE REÇU ==========
Topic : campuspulse/rooms/A103/data
Salle : A103
Température : 30.9 °C
Humidité : 69.1 %
Présence : False
Luminosité : 241 lux
Éclairage : False
Ventilation : True
==================================
```

## 8. Structure du simulateur Python

```text
CampusPulse/
│
├── iot-simulator/
│   │
│   ├── config/
│   │   └── rooms.json
│   │
│   ├── simulators/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── room_simulator.py
│   │   └── mqtt_client.py
│   │
│   ├── requirements.txt
│   └── .venv/
│
└── README.md
```

Le dossier `.venv` est créé localement sur chaque ordinateur et ne doit pas être partagé sur GitHub.

## 9. Remarques importantes

- Une connexion Internet est nécessaire pour communiquer avec HiveMQ.
- Chaque salle doit utiliser un topic MQTT différent.
- Les simulations Python et Wokwi peuvent fonctionner simultanément.
- Ne pas modifier les noms des topics sans modifier également les abonnements MQTT.
- Le broker HiveMQ public est partagé : ne pas y publier de données sensibles.

---

**Projet : CampusPulse – Smart Classroom IoT Monitoring**