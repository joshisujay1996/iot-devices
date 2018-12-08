
from time import sleep
import CoapClientConnector

#this is call when we wan to start the application
def startApp():
    #calling the client connector
    clientApp = CoapClientConnector.CoapClient()
    #resoure her is get_temprature saame as taht of server
    resource = "get_temperature"
    #payload is what the data which needs to be sent
    payload = "Coapclinet in RPi to CoapServer in gateway"
    #below handling post and get requests
    clientApp.PostRequestHandler(resource, payload)
    clientApp.GetRequestHandler(resource)
