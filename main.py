from rollo import Rollo
from umqtt.simple import MQTTClient

SERVER = '192.168.1.22'  # MQTT Server Address (Change to the IP address of your Pi)
CLIENT_ID = 'Blind_1'
TOPICStatus = b'BlindStatus_1'
TOPICRemote = b'BlindREmote_1'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()   # Connect to MQTT broker

while True:
    try:
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):  # Confirm sensor results are numeric
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            client.publish(TOPIC, msg)  # Publish sensor data to MQTT topic
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')