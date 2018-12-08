from coapthon.client.helperclient import HelperClient
import ConfigUtil
import ConfigConst
class CoapClient(object):
    config = None
    serverAddr = None
    host = "localhost"
    port = 5683

    def __init__(self):
        self.config=ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()

        self.host = self.config.getProperty(ConfigConst.COAP_CLOUD_SECTION, ConfigConst.CLOUD_COAP_HOST)
        self.port = int(self.config.getProperty(ConfigConst.COAP_CLOUD_SECTION.CLOUD_COAP_PORT))

        print('\tHost: '+ self.host)
        print('\tPort: '+ self.port)

        if not self.host or self.host.isspace():
            print("Using default host: "+ self.host)

        if self.port < 1024 or self.port>65535:
            print("using default port: "+ self.port)


        self.serverAddr = (self.host, self.port)
        self.url = "coap://"+self.host+":"+str(self.port)

    def initClient(self):
        try:
            self.client = HelperClient(server=("192.171.241.8", 5683))
            print("Created Reference: "+ str(self.client))
            print("  coap://"+self.host+ ":" + str(self.port))

        except Exception:
            print("Failed to Connect to client: "+ self.host)
            pass

    def GetRequestHandler(self,resource):
        print("Testing GET for resource: "+ resource)

        self.initClient()

        response = self.client.get(resource)

        if response:
            print("FROM SERVER: "+response.pretty_print())
            print("WithPAYLOAD: "+ response.payload)

        else:
            print("No response for the GET request: "+ resource)

        self.client.stop()


    def PostRequestHandler(self, resource, payload):
        print("Test POST for resource: "+ resource)

        self.initClient()

        response = self.client.post(resource, payload)

        if response:
            print("Server Response to POST: "+ response.pretty_print())


        else:
            print("No response for the POST requeste: "+ resource)

        self.client.stop()


    def PutRequestHandler(self, resource, payload):
        print("Test PUT for resource: "+ resource)

        self.initClient()

        response = self.client.put(resource, payload)

        if response:
            print("Server Response to PUT: "+response.pretty_print())

        else:
            print("No response for the PUT request: "+ resource)

        self.client.stop()


    def DeleteRequestHandler(self, resource, payload):
        print("Testing DELETE for resource: "+ resource)

        self.initClient()

        response = self.client.delete(resource)

        if response:
            print("Server Response to delete: "+response.pretty_print())

        else:
            print("No response for the DELETE request: "+ resource)

        self.client.stop()


    def ServerPing(self):

        print("ping to server")

        self.initClient()
