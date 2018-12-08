from coapthon.server.coap import CoAP
import ConfigUtil
import ConfigConst
import CoapResourceHandler

#this class implements coap class
class CoapServerConnector(CoAP):

    config=None
#constructors for the class
#the ip address is given to say it forver one in world can access
    def __init__(self, ipAddr = "0.0.0.0", port = 5683, multicast = False):
        self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        CoAP.__init__(self, (ipAddr, port), multicast)
        if port >= 1024:
            self.port = port
        else:
            #port number to connect by default
            self.port = 5683
        self.ipAddr   = ipAddr
        self.useMulticast = multicast
        self.initResources()

    def TestCoapResource(self):
        #just to test
        print("Testing")


#adding the resoure with value given is "get_temprature" 
    def initResources(self):
        self.add_resource('get_temperature', CoapResourceHandler.TestCoapResource())
        print("CoAP server started. Binding: " + self.ipAddr + ":" + str(self.port))
        print(self.root.dump())
