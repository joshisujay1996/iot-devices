from coapthon.server.coap import CoAP
import ConfigUtil
import ConfigConst
from CoapResourceHandler import CoapResource

#this is used in the coap server app to run the server
class CoapServerConnector(CoAP):

    config=None
#constructor
    def __init__(self, ipAddr = "0.0.0.0", port = 5683, multicast = False):
        self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        CoAP.__init__(self, (ipAddr, port), multicast)
        if port >= 1024:
            self.port = port
        else:
            self.port = 5683
        self.ipAddr   = ipAddr
        self.useMulticast = multicast
        self.initResources()
#tesing
    def CoapResource(self):
        print("Testing")


#adding resource with value get_temprature
    def initResources(self):
        self.add_resource('get_temperature', CoapResourceHandler.CoapResource())
        print("CoAP server started. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())
