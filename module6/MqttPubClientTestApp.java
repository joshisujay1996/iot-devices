package org.joshisuj.labs.iot.IOT;
import java.util.logging.Logger;
//this calls is instantiation the mqttpubclienttestapp and running it
public class MqttPubClientTestApp {
	private static final Logger _Logger = Logger.getLogger(MqttPubClientTestApp.class.getName());
	private static MqttPubClientTestApp _App;

	public static void main(String[] args)
	{
	_App = new MqttPubClientTestApp();
	try {
	_App.start();
	} catch (Exception e) {
	e.printStackTrace();
	}
	}
	private MqttClientConnector _mqttClient;

	public MqttPubClientTestApp()
	{
	super();
	}

	public void start()
	{
//		here we are connecting to the mqtt broker and sending 3 payload to the broker with topicname test
	_mqttClient = new MqttClientConnector();
	_mqttClient.connect();
	String topicName = "test";
	String payload = "This is a test...";

	_mqttClient.publishMessage(topicName, 0, payload.getBytes());
	_mqttClient.publishMessage(topicName, 1, payload.getBytes());
	_mqttClient.publishMessage(topicName, 2, payload.getBytes());
	_mqttClient.disconnect();
	}
}
