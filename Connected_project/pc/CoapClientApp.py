
from time import sleep
import CoapClientConnector

#this method is called wehn we want to connect to teh server
# it uses methods in coap client connector
def startApp():
    clientApp = CoapClientConnector.CoapClient()
    #resourse here is get_temprature same as server
    resource = "get_temperature"
    #payload is what needs to be sent
    payload = "Coapclinet in gateway to CoapServer in Rpi"
    clientApp.PostRequestHandler(resource, payload)
    clientApp.GetRequestHandler(resource)
    clientApp.disconnectClient()
