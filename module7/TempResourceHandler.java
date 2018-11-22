package org.joshisuj.labs.IOT1.module7;


import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.ExecutorService;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.network.Endpoint;
import org.eclipse.californium.core.network.Exchange;
import org.eclipse.californium.core.observe.ObserveRelation;
import org.eclipse.californium.core.server.resources.CoapExchange;
import org.eclipse.californium.core.server.resources.Resource;
import org.eclipse.californium.core.server.resources.ResourceAttributes;
import org.eclipse.californium.core.server.resources.ResourceObserver;

public class TempResourceHandler extends CoapResource {


	public TempResourceHandler()
	{
		super("temp", false);
	}


//	getting the data inside the text file
	public void handleGET(CoapExchange ce)
	{
		File file = new File("C:\\Users\\Sujay Joshi\\Desktop\\iot_module.txt");
		FileInputStream fis = null;


		try {
			fis = new FileInputStream(file);

			int bytes = fis.available();
			byte[] data = new byte[bytes];
			int count = fis.read(data);

			if(count>0)
			{
				ce.respond(ResponseCode.VALID, new String(data));
			}


		} catch(Exception e)
		{
			e.printStackTrace();
		}


	}

// putting data to the text file
	public void handlePOST(CoapExchange ce)
	{
		File file = new File("C:\\Users\\Sujay Joshi\\Desktop\\iot_module.txt");

		FileOutputStream fos = null;


		try {

			fos = new FileOutputStream(file);

			if(!file.exists())
				file.createNewFile();

			byte[] data = ce.getRequestPayload();

			fos.write(data);

			fos.flush();
			fos.close();

			ce.respond(ResponseCode.VALID, "Success");


		} catch(Exception e)
		{
			e.printStackTrace();
		}

	}
//appending to the posted text content
	public void handlePUT(CoapExchange ce)
	{
		File file = new File("C:\\Users\\Sujay Joshi\\Desktop\\iot_module.txt");

		FileOutputStream fos = null;


		try {

			fos = new FileOutputStream(file, true);

			if(!file.exists())
				file.createNewFile();

			byte[] data = ce.getRequestPayload();

			fos.write(data);

			fos.flush();
			fos.close();

			ce.respond(ResponseCode.VALID, "Success");


		} catch(Exception e)
		{
			e.printStackTrace();
		}

	}

//deleting the content inside the text file
	public void handleDELETE(CoapExchange ce)
	{
		File file = new File("");


		try {

			PrintWriter pw = new PrintWriter(file);

			pw.close();

			ce.respond(ResponseCode.VALID, "Success");


		} catch(Exception e)
		{
			e.printStackTrace();
		}

	}



}