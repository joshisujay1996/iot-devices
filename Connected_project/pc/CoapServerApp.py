import CoapServerConnector
import UbiSubscribe

class CoapServerApp:

    def ConnectApp(self):
        ipAddr       = "0.0.0.0"
        port         = 5683
        useMulticast = False
        coapServer   = None

        try:
            UbiSubscribe.getMe()
            CoapServer = CoapServerConnector.CoapServerConnector(ipAddr, port, useMulticast)
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
