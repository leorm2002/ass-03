import time
import ubinascii
from umqtt.simple import MQTTClient
import machine
import random
from fakesonar import FakeSonar
from hcsr04 import HCSR04
from constants import TRIG_PIN, ECHO_PIN, DEFAULT_FREQ, MQTT_BROKER, SUBSCRIBE_TOPIC, PUBLISH_TOPIC
import json
CLIENT_ID = ubinascii.hexlify(machine.unique_id())

# Publish MQTT messages after every set timeout
last_sample = time.time()
publish_interval = DEFAULT_FREQ

# Creo l'oggetto sonar
sonar = HCSR04(trigger_pin=TRIG_PIN, echo_pin=ECHO_PIN, echo_timeout_us=10000)


def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()


def to_num_or_none(s):
    try:
        s = json.loads(s)
        if "frequency" not in s:
            return None
        s = s["frequency"]
        return int(s)
    except:
        return None

def get_level_reading():
    level = sonar.distance_cm()
    print("Sampled: ", level)
    return level

def set_sampling_frequency(topic, msg):
    global publish_interval
    freq = to_num_or_none(msg.decode())
    if freq:
        print("Nuova frequenza ", freq)
        publish_interval =  60 / freq
def format_level(level):
    return f"{{\"level\":{level}}}"
    
def main():
    print(f"Inizio connessione con :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    mqttClient.set_callback(set_sampling_frequency)
    mqttClient.connect()
    mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connesso a :: {MQTT_BROKER}")
    LedManager().green_mode()
    while True:
            # Non-blocking wait for message
            mqttClient.check_msg()
            global last_sample
            if (time.time() - last_sample) >= publish_interval:
                random_temp = get_level_reading()
            
                msg =format_level(random_temp)
                mqttClient.publish(PUBLISH_TOPIC, msg.encode())
                last_sample = time.time()
            time.sleep(0.1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            LedManager().red_mode()
            print("Error: " + str(e))
            reset()

