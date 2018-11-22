package org.joshisuj.labs.IOT1.module7;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;

public class CoapServerConnection {

	private static final Logger _logger = Logger.getLogger(CoapServerConnection.class.getName());
	private CoapServer _coapServer;

	public CoapServerConnection()
	{
		super();
	}

	public void addResource(CoapResource resource)
	{
		if (resource!=null)
			_coapServer.add(resource);
	}

	public void start()
	{
//		starting the server
		if(_coapServer==null)
		{
			_logger.info("creating coap server instance and 'temp' handler...");
			_coapServer = new CoapServer();
			TempResourceHandler tempHandler = new TempResourceHandler();
			_coapServer.add(tempHandler);

		}

		_logger.info("Starting the CoAP server...");
		_coapServer.start();
	}
//	to stop the server
	public void stop()
	{
		_logger.info("stopping the CoAP server");
		_coapServer.stop();
	}



}
