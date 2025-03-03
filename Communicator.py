import serial
import time


class Communicator():
    
    # init for when specific com port is known
    # comPort = serialPort number that microcontroller is connected to
    # response setting: if set to true, sendCommand will return false if "done" is not returned over serial
    def __init__(self, comPort, defaultResponseSetting):
        # set the com port and open serial
        self.COM_PORT = "\\\\.\\COM"  + comPort
        self.serialRead = serial.Serial(
            port=self.COM_PORT,
            baudrate=9600,
            bytesize=8,
            timeout=2,
            stopbits=serial.STOPBITS_ONE
        )
        # time to wait in between sends over serial to ensure it goes through
        self.WAIT_TIME = 2
        self.RESPONSE_SETTING = defaultResponseSetting
        
    # for if messages arent going through, set the wait time to a lower value
    def setWaitTime(self, newWaitTime):
        self.WAIT_TIME = newWaitTime
    
    # change the response setting
    def setResponseSetting(self, newResponseSetting):
        self.RESPONSE_SETTING = newResponseSetting
        
    # if response setting is set to true, listen for response and return false if "done" response not recieved
    # returns true if done response recieved
    def confirmMessage(self):
        NUM_TRYS = 10
        for i in range(NUM_TRYS):
            response = self.serialRead.readline()
            if(response == "done"):
                return True
        return False
        
    # sends a command with paramaters given in array parsed as strings
    # sends each parameter on a new line for arduino to parse
    def sendCommand(self, command, params):
        self.serialRead.write(str.encode(command + "\n"))
        for param in params:
            self.serialRead.write(str.encode(str(param + "\n")))
            
        
    
    