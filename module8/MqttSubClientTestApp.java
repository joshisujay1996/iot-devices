package prg.joshisuj.labs.iot.module8;
import java.util.logging.Logger;

public class MqttSubClientTestApp {

	Logger _logger = Logger.getLogger(MqttSubClientTestApp.class.getName());

	String token = "A1E-ntVJzB9Nm7a9ai9EN6AZJsjqTKXRHp";
	String pemFileName = "/home/ashwath/Downloads/connectedDocs/ubidots.pem";

	private static MqttSubClientTestApp _App;
	private MqttClientConnector _clientConn;

//	suscribing to the specfic mqtt topic and getting response
	public MqttSubClientTestApp() {
		super();
	}

	public static void main(String[] args) {

		_App = new MqttSubClientTestApp();

		try {
			_App.start();
		}catch(Exception e)
		{
			e.printStackTrace();
		}


	}

	public void start()
	{
		_clientConn = new MqttClientConnector("things.ubidots.com", token, pemFileName);
		_clientConn.connect();

		String topicName = "/v1.6/devices/homeiotgateway/tempactuator/lv";;


		_clientConn.subscribeToTopic(topicName);



	}
}
