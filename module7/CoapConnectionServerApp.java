package org.joshisuj.labs.IOT1.module7;

import java.util.logging.Level;
import java.util.logging.Logger;
// to run the server
public class CoapConnectionServerApp {

	private static final Logger _logger = Logger.getLogger(CoapConnectionServerApp.class.getName());
	private static CoapConnectionServerApp _app = null;
	private CoapServerConnection coapServerConnect;

	public CoapConnectionServerApp()
	{
		super();

	}

	public static void main(String[] args) {


		_app = new CoapConnectionServerApp();

		try {
			_app.start();
		}catch(Exception e)
		{
			_logger.log(Level.SEVERE, "Server not running", e);
		}

	}

	public void start()
	{
		coapServerConnect = new CoapServerConnection();
		coapServerConnect.start();
	}

}
