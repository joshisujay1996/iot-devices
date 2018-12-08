import paho.mqtt.client as mqttClient
import time
import json
import ssl

'''
global variables
'''

connected = False  # Stores the connection statu
BROKER_ENDPOINT = "things.ubidots.com"
TLS_PORT = 8883  # Secure port
MQTT_USERNAME = ""  # Put here your Ubidots TOKEN
MQTT_PASSWORD = ""  # Leave this in blank
# TOPIC = "/v1.6/devices/homeiotgateway/tempsensor"
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "projectiot/actuatetemprature"
TLS_CERT_PATH = "/home/sujay/Desktop/git/Connected_devices_project/Module8_python/ubidots.cert"
'''
Functions to process incoming and outgoing streaming
'''
#thsi method defines what needs to be done on connec to mqtt server
def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")
#this method is defies to get the message and display 
def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload) + " OK. Payload received")
#subscribing to specfic topic 
def on_subscribe(self, client, userdata, result):
    print("Subscribe Success!")

#this method is used to connect to the mqtt brokerusing user id and certification
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected
#if not connected, try to connect
    if not connected:
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe

        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0
#try to connect again and agian, for 5 attempts
        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1
#still not able to connect then there is some issue
    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True

#subscribing to specfic topic
def subscribe(mqtt_client, topic, payload):

    try:
        mqtt_client.subscribe(topic, payload)

    except Exception as e:
        print("[ERROR] Could not subscribe data, error: {}".format(e))

#this function will be called to get the message from topic
def getMe():
    # val1 = 39
    # payload = json.dumps({"value": val1 })
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)
    # # topic = TOPIC

    mqtt_client = mqttClient.Client()

    if not connect(mqtt_client, MQTT_USERNAME,
                   MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
        return False

    payload = 1
    # payload is qos level here
    data = subscribe(mqtt_client, topic, payload)
    # print(data)
    # mqtt_client.subscribe(topic)
    mqtt_client.on_message = on_message
    return True
