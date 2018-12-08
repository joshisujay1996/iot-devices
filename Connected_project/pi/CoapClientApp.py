
from time import sleep
import CoapClientConnector

def startApp():
    clientApp = CoapClientConnector.CoapClient()
    resource = "get_temperature"
    payload = "Coapclinet in RPi to CoapServer in gateway"
    clientApp.PostRequestHandler(resource, payload)
    clientApp.GetRequestHandler(resource)
