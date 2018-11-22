package org.joshisuj.labs.iot.IOT;
import java.util.logging.Logger;
//here we are instatiting mqttsubclient test app adn then running it
public class MqttSubClientTestApp {
	private static final Logger _Logger = Logger.getLogger(MqttSubClientTestApp.class.getName());
	private static MqttSubClientTestApp _App;

	public static void main(String[] args)
	{
	_App = new MqttSubClientTestApp();
	try {
	_App.start();
	} catch (Exception e) {
	e.printStackTrace();
	}
	}
	private MqttClientConnector _mqttClient;

	public MqttSubClientTestApp()
	{
	super();
	}

	public void start()
	{
//		connecting to mqtt and the suscribing to topic with name test
	_mqttClient = new MqttClientConnector();
	_mqttClient.connect();
	String topicName = "test";
	_mqttClient.subscribeToTopic(topicName);


	}
}
