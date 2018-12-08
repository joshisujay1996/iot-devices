package prg.joshisuj.labs.iot.module8;

import java.util.Random;
import java.util.logging.Logger;
import org.json.simple.JSONObject;


public class MqttPubClientTestApp {


	Logger _logger = Logger.getLogger(MqttPubClientTestApp.class.getName());
//	api in the ubi dots after login os put on place of token
//	pemfile loction shouled be provided
	String token = "";
	String pemFileName = "/home/sujay/Desktop/git/Connected_devices_project/Module8_python/ubidots.cert";

	private static MqttPubClientTestApp _App;
	private MqttClientConnector _clientConn;

	public MqttPubClientTestApp() {
		super();
	}

	public static void main(String[] args) {

		_App = new MqttPubClientTestApp();

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
//		name of the topic which we want to connet to
		String topicName = "/v1.6/devices/HomeIotGateway/tempsensor";

		String payload;
		JSONObject obj = new JSONObject();


		Random rand = new Random();
		int val = rand.nextInt(45) +1;
		obj.put("value", val);
		payload = obj.toJSONString();
		_clientConn.publishMessage(topicName, 0, payload.getBytes());


		_clientConn.disconnect();

	}

}
