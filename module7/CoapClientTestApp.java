package org.joshisuj.labs.IOT1.module7;


import java.util.logging.Logger;
// to test teh coapClientTestApp
public class CoapClientTestApp {

	private static final Logger _logger = Logger.getLogger(CoapClientTestApp.class.getName());
	private static CoapClientTestApp _app;
	private CoapClientConnector _coapClient;

	public CoapClientTestApp()
	{
		super();

	}

	public static void main(String[] args) {

		_app = new CoapClientTestApp();

		try {
			_app.start();
		}catch(Exception e)
		{
			e.printStackTrace();
		}

	}

	public void start()
	{
		_coapClient = new CoapClientConnector();
		_coapClient.runTests("temp");
	}

}
