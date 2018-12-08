import CoapServerConnector

#this is importing teh coap server implemented and will run the server
class CoapServerApp:

    def ConnectApp(self):
        ipAddr       = "0.0.0.0"
        port         = 5683
        useMulticast = False
        coapServer   = None

        try:
            #calling the server connecter and try to connect
            CoapServer = CoapServerConnector.CoapServerConnector(ipAddr, port, useMulticast)
            #TRY AND CATCH BLOCK IS USED TO HANDLE IS THERE ARE ANY ERRORS
            try:
                #listining if anyone wants to connect
                coapServer.listen(10)
                print("Created link to server: " + str(coapServer))
            except Exception:
                print("Failed to connect to Server with ip : " + ipAddr)
                pass
        except KeyboardInterrupt:
            print("KeyboardInterrupt Closing!!!")
#CLOSE this if connected
        if CoapServer:
            coapServer.close()

        print("CoAP server ending.")
