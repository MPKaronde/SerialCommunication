import serial
import time

# time to sleep between sends in ms (avoid error from sending too fast)
WAIT_TIME = 2

# handles basic communication tasks (sending and recieving value)
class simpleCommunicator:
    
    # port = string port address (ex: "\\\\.\\COM7")
    # TODO: implement automatic port detection
    def __init__(self, port):
        self.COM_PORT = port
        self.serialRead = serial.Serial(
            port=self.COM_PORT,
            baudrate=9600,
            bytesize=8,
            timeout=2,
            stopbits=serial.STOPBITS_ONE
        )
    
    # sends given command on new line in serial
    # command must be a string to work correctly
    def sendString(self, command):
        time.sleep(WAIT_TIME)
        self.serialRead.write(str.encode(command))
    
    # sends given value on new line in serial
    # value is assumed to be a number value that can be cast to a string
    def sendValue(self, value):
        self.sendString(str(value))
        
    # reads latest sent value on serial and returns it
    def readPort(self):
        return self.serialRead.readline()
    
    # sends command followed by each item in parameters seperated by spaces
    # command is a string
    # param is an array of string castable values
    # the sent command includes a space after command, a space between each param
    #   and a space after the final param before the line terminator
    def sendCommandWithParameters(self, command, param):
        sendData = command + " "
        for i in param:
            sendData += str(i)
            sendData += " "
        self.sendString(sendData)
            
        
        
        