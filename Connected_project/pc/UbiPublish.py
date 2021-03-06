# imports below
import paho.mqtt.client as mqttClient
import time
import json
import ssl

'''
global variables
'''

connected = False  # Stores the connection status
# to connect to educational ubidots
BROKER_ENDPOINT = "things.ubidots.com"
TLS_PORT = 8883  # Secure port
MQTT_USERNAME = ""  # Put here your Ubidots TOKEN
MQTT_PASSWORD = ""  # Leave this in blank
# TOPIC = "/v1.6/devices/homeiotgateway/tempsensor"
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "projectiot/sensetemprature"
TLS_CERT_PATH = "/home/sujay/Desktop/git/Connected_devices_project/Module8_python/ubidots.cert"
'''
Functions to process incoming and outgoing streaming
'''
#what to do on_connection if what this definition is
#we will connect and print logs
def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")

#method is used to publish the message to mqtt server
def on_publish(client, userdata, result):
    print("Published!")

#try to connect to mqtt server if sucessfull go and publish
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected
#if not able to connect then the block belwo will run
    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0
#try to connect again and agian, 5 attenmpts
        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1

#if still not able to connect then print error            
    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True

#used to publish this to ubidots with given topic name and payload
def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))

#this method is calledin other class when we want to publish to ubidots
def tempPublish(val1):
    payload = json.dumps({"value": val1 })
    # print(type(payload))
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)
    # topic = TOPIC

    mqtt_client = mqttClient.Client()

    if not connect(mqtt_client, MQTT_USERNAME,
                   MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
        return False
    i=0
    while(i<5):
        publish(mqtt_client, topic, payload)
        time.sleep(10)
        i=i+1
    return True
