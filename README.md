# **SerialCommunication**
### __Simplifies communication with arduino, esp32 and other such boards__

## Use: simpleCommunicator.py:
### Instantiate a simpleCommunicator object 
port is a string representing the address of the COM port you're board is connected to you're computer with  
    For example: if connected on COM port 7, would use "\\\\.\\COM7"  
    __An easy way to check the address of you're port is to check what port you're Arduino IDE autodetects you're board to be on__  
__TODO__: in future will add autodetect abilities
### sendString:
accepts a command python string
encodes this string to UTF-8 and sends it over the serial port
### sendValue:
intended to send number values (ints, floats, etc), but can be used for anything that casts to a string
casts value to string, encodes to UTF-8, and sends it over serial
### readData:
reads the latest line sent over serial and returns it as a string
### sendCommandWithParameters:
used for sending some command with parameters for execution
command is expected to be a string
params is expected to be an array of values that can be cast to string (strings, number vals, etc)
sends everything together in one line with spaces between each value and a trailing space for interpretation by arduino
__TODO__: make arduino intepreter module



