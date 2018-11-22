package org.joshisuj.labs.IOT1.module7;

import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResponse;
import org.eclipse.californium.core.WebLink;
import org.eclipse.californium.core.coap.MediaTypeRegistry;

public class CoapClientConnector
{

	private static final Logger _logger = Logger.getLogger(CoapClientConnector.class.getName());

//	we need to tell which protocol we are using, host here is local as the coap server has been implemented
	private String  _protocol = "coap";
	private String  _host = "127.0.0.1";
	private int     _port = 5683;
	private String  _connUrl = null;
	private CoapClient _coapClient;
	private String  _serverAddr;
	private boolean isInitialized;


	public CoapClientConnector()
	{
		this("127.0.0.1", false);
	}

	public CoapClientConnector(String host, boolean isSecure)
	{
		super();
		if (host!=null && host.trim().length()>0)
		{
			_host=host;
		}
//		summing all the data entered above
		_serverAddr = _protocol + "://" + _host + ":" + _port;
		_connUrl = _serverAddr;
		_logger.info("URL for the connection: "+ _serverAddr);
	}


	public void runTests(String resourceName)
	{
		try {
			isInitialized = false;

			initClient(resourceName);

			_logger.info("current URL: "+ getCurrentUri());

			String payload = "Sample payload";

			pingServer();
			discoverResources();
			displayResources();
			sendGetRequest();
			sendGetRequest(true);
			sendPostRequest(payload, false);
			sendPostRequest(payload, true);
			sendPutRequest(payload, false);
			sendPutRequest(payload, true);
			sendDeleteRequest();


		}catch(Exception e)
		{
			_logger.log(Level.SEVERE, "Failed to issue request to CoAP server", e);
		}

	}

	public String getCurrentUri()
	{
		return (_coapClient !=null ? _coapClient.getURI(): _serverAddr);
	}

	public void discoverResources()
	{
		_logger.info("issuing discover...");

		initClient();

		Set<WebLink> wlSet = _coapClient.discover();

		if(wlSet != null)
		{
			for(WebLink wl:wlSet)
				_logger.info("--> WebLink: "+ wl.getURI());
		}

	}

    public void pingServer()
    {
//    	this method is to ping the server
    	_logger.info("sending ping...");

    	initClient();

    	if(_coapClient.ping())
    	{
    		_logger.info("Ping successful!");
    	}
    }


    public void sendGetRequest()
    {
//    	sending get request
    	initClient();
    	handleGetRequest(false);
    }

    public void sendGetRequest(String resourceName)
    {
    	isInitialized = false;
    	initClient(resourceName);
    	handleGetRequest(false);
    }

    public void sendGetRequest(boolean useNON)
    {
    	initClient();
    	handleGetRequest(useNON);
    }

    public void sendPostRequest(String payload, boolean useCON)
    {
    	initClient();
    	handlePostRequest(payload, useCON);
    }

    public void sendPostRequest(String resourceName, String payload, boolean useCON)
    {

    	isInitialized = false;
    	initClient(resourceName);
    	handlePostRequest(payload, useCON);
    }

    public void sendPutRequest(String payload, boolean useCON)
    {
    	initClient();
    	handlePutRequest(payload, useCON);
    }

    public void sendPutRequest(String resourceName, String payload, boolean useCON)
    {
    	isInitialized = false;
    	initClient(resourceName);
    	handlePutRequest(payload, useCON);
    }

    public void sendDeleteRequest()
    {
    	initClient();

    	handleDeleteRequest(false);
    }

    public void sendDeleteRequest(String resourceName)
    {
    	isInitialized = false;

    	initClient(resourceName);

    	handleDeleteRequest(false);
    }

    public void displayResources()
    {
    	initClient();
    	_logger.info("getting all remote web links...");

    	Set<WebLink> webLinkSet = _coapClient.discover();

    	for(WebLink wl:webLinkSet)
    	{
    		_logger.info(wl.getURI());
    	}

    }

    public void Request()
    {
    	sendGetRequest(null);
    }

    private void initClient(String resourceName)
    {
    	if(isInitialized)
    	{
    		return;
    	}


    	if(_coapClient!=null)
    	{
    		_coapClient.shutdown();
    		_coapClient = null;

    	}
    	try {
    		if(resourceName != null)
    		{
    			_serverAddr += "/"+resourceName;

    		}

    		_coapClient = new CoapClient(_serverAddr);

    		_logger.info("Created client connection to server / resource: "+_serverAddr);

    	}
    	catch(Exception e)
    	{
    		_logger.log(Level.SEVERE,"Failed to connect to broker: "+getCurrentUri(), e);
    	}
    }

    private void initClient()
    {
    	initClient(null);
    }


    private void handleDeleteRequest(boolean useNON)
    {

    	_logger.info("Sending DELETE request...");

    	CoapResponse response = null;
    	if(useNON)
    	{
    		_coapClient.useNONs().useEarlyNegotiation(32).get();
    	}

    	response = _coapClient.delete();

    	if(response!=null)
    	{
    		_logger.info("Response: "+response.isSuccess()+"-"+response.getOptions()+"-"+response.getCode());
    	}
    	else {
    		_logger.warning("No response received");
    	}

    	_logger.info("RESPONSE FROM THE SERVER: " + response.getResponseText());

    }

    private void handleGetRequest(boolean useNON)
    {

    	_logger.info("Sending GET request...");

    	CoapResponse response = null;
    	if(useNON)
    	{
    		_coapClient.useNONs().useEarlyNegotiation(32).get();
    	}

    	response = _coapClient.get();

    	if(response!=null)
    	{
    		_logger.info("Response: "+response.isSuccess()+"-"+response.getOptions()+"-"+response.getCode());
    	}
    	else {
    		_logger.warning("No response received");
    	}

    	_logger.info("RESPONSE FROM THE SERVER: " + response.getResponseText());

    }

    private void handlePutRequest(String payload, boolean useCON)
    {
    	_logger.info("sending PUT....");
    	CoapResponse response = null;
    	if(useCON)
    	{
    		_coapClient.useCONs().useEarlyNegotiation(32).get();
    	}

    	response = _coapClient.put(payload, MediaTypeRegistry.TEXT_PLAIN);

    	if(response!=null)
    	{
    		_logger.info("Response: "+response.isSuccess()+"-"+response.getOptions()+"-"+response.getCode());
    	}
    	else {
    		_logger.warning("No response received");
    	}

    	_logger.info("RESPONSE FROM SERVER: "+ response.getResponseText());

    }

    private void handlePostRequest(String payload, boolean useCON)
    {
    	_logger.info("sending POST");
    	CoapResponse response= null;
    	if(useCON)
    	{
    		_coapClient.useCONs().useEarlyNegotiation(32).get();
    	}

    	response = _coapClient.post(payload, MediaTypeRegistry.TEXT_PLAIN);

    	if(response!=null)
    	{
    		_logger.info("Response:" + response.isSuccess() + "-" + response.getOptions() +"-" + response.getCode());
    	}else {
    		_logger.warning("No response received");
    	}

    	_logger.info("RESPONSE FROM SERVER: "+ response.getResponseText());

    }





}
