
from time import sleep
import CoapClientConnector

def startApp():
    clientApp = CoapClientConnector.CoapClient()
    resource = "get_temperature"
    payload = "Coapclinet in gateway to CoapServer in Rpi"
    clientApp.PostRequestHandler(resource, payload)
    clientApp.GetRequestHandler(resource)
    clientApp.disconnectClient()
