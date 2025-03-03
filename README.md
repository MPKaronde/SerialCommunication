# **SerialCommunication**
### __Simplifies communication with arduino, esp32 and other such boards__

## Use: Communicator.py:
### Instantiate a simpleCommunicator object 
comPort: what serialPort your using
baudRate: 9600 should work well for most boards, can experiment with higher ones in Arduino IDE if needed and use what works
defaultResponseSetting: when true, sendCommand will return true if and only if a message of "done" is sent after the message is sent
    __An easy way to check the address of you're port is to check what port you're Arduino IDE autodetects you're board to be on__  

### sendCommand:
Sends "command" (the command identifier) one one line and each parameters from the "params" list on successive lines.
If defaultResponseSetting is true, will return false if "done" is not recieved over serial upon completion

### readResponse:
Reads numLines off of serial port back, concatinates those lines into one (newLine seperated) string, and returns that string



