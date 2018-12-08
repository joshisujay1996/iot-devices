from coapthon.resources.resource import Resource
import UbiPublish
import UbiIntruderPublish

class CoapResource(Resource):

    def __init__(self, name= "CoapResource", coap_server = None):
        super(CoapResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Test Coap Resource"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"


    def Get_req(self, request):
        print("successfully retrieved this message from CoapResource. Payload: "+ str(self.payload))
        file_handler = open("/home/sujay/Documents/connectedFile.txt", "r")
        self.payload = file_handler.read()
        file_handler.close()
        return self

    def Post_req(self, request):
        res = CoapResource()
        file_handler = open("/home/sujay/Documents/connectedFile.txt", "w")
        res.payload = request.payload
        file_handler.write(request.payload)
        file_handler.close()
        UbiPublish.tempPublish(1)
        UbiIntruderPublish.intruderPublish(1)
        return res
    def Delete_req(self, request):
        self.payload = request.payload
        file_handler = open("/home/sujay/Documents/connectedFile.txt", "w")
        file_handler.close()
        return True

    def Put_req(self, request):
        self.payload = request.payload
        file_handler = open("/home/sujay/Documents/connectedFile.txt", "a")
        file_handler.write(self.payload)
        file_handler.close()
        return self
