import CoapServerConnector
import UbiSubscribe
#the server app will use the coap server class to run its methods  and act as server
class CoapServerApp:

    def ConnectApp(self):
        ipAddr       = "0.0.0.0"
        port         = 5683
        useMulticast = False
        coapServer   = None

        try:
            #this will call the ubisubscribe class and it method to subscribeto relevant topic
            UbiSubscribe.getMe()
            CoapServer = CoapServerConnector.CoapServerConnector(ipAddr, port, useMulticast)
            #handling excepition
            try:
                coapServer.listen(10)
                print("Created link to server: " + str(coapServer))
            except Exception:
                print("Failed to connect to Server with ip : " + ipAddr)
                pass
        except KeyboardInterrupt:
            print("KeyboardInterrupt Closing!!!")

        if CoapServer:
            coapServer.close()

        print("CoAP server ending.")
