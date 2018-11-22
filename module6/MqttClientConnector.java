package org.joshisuj.labs.iot.IOT;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttClientConnector implements MqttCallback
{
 private static final Logger _Logger = Logger.getLogger(MqttClientConnector.class.getName());
 private String _protocol = "tcp";
 private String _host = "iot.eclipse.org";
 private int _port = 1883;
 private String _clientID;
 private String _brokerAddr;
 private MqttClient _mqttClient;


 public MqttClientConnector()
 {
 this(null, false);
 }

  public MqttClientConnector(String host, boolean isSecure)
  {
  super();
  if (host != null && host.trim().length() > 0) {
  _host = host;
  }
  _clientID = MqttClient.generateClientId();
  _Logger.info("Using client ID for broker conn: " + _clientID);
  _brokerAddr = _protocol + "://" + _host + ":" + _port;
  _Logger.info("Using URL for broker conn: " + _brokerAddr);
  }

  public void connect()
  {
  if (_mqttClient == null) {
  //Persistence that uses memory In cases where reliability is not required across client or device restarts memory this memory peristence can be used.
  //In cases where reliability is required like when clean session is set to false then a non-volatile form of persistence should be used.
  MemoryPersistence persistence = new MemoryPersistence();
  try {
  _mqttClient = new MqttClient(_brokerAddr, _clientID, persistence);
  MqttConnectOptions connOpts = new MqttConnectOptions();
  connOpts.setCleanSession(true);
  _Logger.info("Connecting to broker: " + _brokerAddr);
  _mqttClient.setCallback(this);
  _mqttClient.connect(connOpts);
  _Logger.info("Connected to broker: " + _brokerAddr);
  } catch (MqttException e) {
  _Logger.log(Level.SEVERE, "Failed to connect to broker: " + _brokerAddr, e);
  }
  }
  }
//  disconnecting after the process is done, ie., publish and suscribe
  public void disconnect()
  {
  try {
  _mqttClient.disconnect();
  _Logger.info("Disconnected from broker: " + _brokerAddr);
  } catch (Exception e) {
  _Logger.log(Level.SEVERE, "Failed to disconnect from broker: " + _brokerAddr, e);
  }
  }
//publishing the message to mqtt
  public boolean publishMessage(String topic, int qosLevel, byte[] payload)
  {
  boolean success = false;
  try {
  _Logger.info("Publishing message to topic: " + topic);
  MqttMessage mqttMsg = new MqttMessage();
	mqttMsg.setQos(qosLevel);

	_mqttClient.publish(topic, mqttMsg);

	_Logger.info("published message ID: "+mqttMsg.getId());


	success=true;
  } catch (Exception e) {
  _Logger.log(Level.SEVERE, "Failed to publish MQTT message: " + e.getMessage());
  }
  return success;
  }
  public boolean subscribeToAll()
  {
  try {
  _mqttClient.subscribe("$SYS/#");
  return true;
  } catch (MqttException e) {
  _Logger.log(Level.WARNING, "Failed to subscribe to all topics.", e);
  }
  return false;
  }
  public boolean subscribeToTopic(String topic)
  {
	 try {
		 _mqttClient.subscribe(topic);
		 return true;
	 }catch(MqttException e) {
		 _Logger.log(Level.WARNING, "Failed to subscribe to the current topic.", e);
	 }
	 return false;
  }
//  Enables an application to be notified when asynchronous events related to the client occur. Classes implementing this interface can
//  be registered on both types of client: IMqttClient.setCallback(MqttCallback) and IMqttAsyncClient.setCallback(MqttCallback)
  public void connectionLost(Throwable t)
  {

  _Logger.log(Level.WARNING, "Connection to broker lost. retrying now.", t);
  connect();

  }
  /*
  * Enables an application to be notified when asynchronous events related to the client occur. Classes implementing this interface can
  *  be registered on both types of client: IMqttClient.setCallback(MqttCallback) and IMqttAsyncClient.setCallback(MqttCallback)
  */
  public void deliveryComplete(IMqttDeliveryToken token)
  {
  // logging the delivaryMessage, getting token and get response
  try {
	  _Logger.info("Delivery complete: " + token.getMessageId() + " - " + token.getResponse() + " - "
			  + token.getMessage());
			  } catch (Exception e) {
			  _Logger.log(Level.SEVERE, "Failed to retrieve message from token.", e);
			  }
			  }

public void messageArrived(String data, MqttMessage msg) throws Exception
{
//getting the message, message id and the message from the subscribed topic
 _Logger.info("Message arrived: " + data + ", " + msg.getId() +  " This is a test..."+ msg);
 }
}
