# **SerialCommunication**
### __Simplifies communication with arduino, esp32 and other such boards__

## Use: simpleCommunicator.py:
<div>
### Instantiate a simpleCommunicator object 
port is a string representing the address of the COM port you're board is connected to you're computer with  
    For example: if connected on COM port 7, would use "\\\\.\\COM7"  
    __An easy way to check the address of you're port is to check what port you're Arduino IDE autodetects you're board to be on__  
<div>
### sendString:
accepts a command python string
encodes this string to UTF-8 and sends it over the serial port
</div>
<div>
    
</div>

