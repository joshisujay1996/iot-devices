'''
Created on Sep 22, 2018

@author: Sujay Joshi
'''

from labs.common import ConfigConst
from labs.common import ConfigUtil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SmtpClientConnector(object):

    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))
        
    def publishMessage(self, topic, data):
        host= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION,ConfigConst.HOST_KEY)
        port= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION,ConfigConst.PORT_KEY)
        fromAddr= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION,ConfigConst.FROM_ADDRESS_KEY)
        toAddr= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY)
        authToken= self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        msg= MIMEMultipart()
        msg['From'] = fromAddr
        msg['To']= toAddr               
        msg['Subject'] = topic        
        msgBody = str(data)
        msg.attach(MIMEText(msgBody))
        msgText= msg.as_string()
        smtpServer= smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
        