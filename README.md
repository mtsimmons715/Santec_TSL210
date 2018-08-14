# Santec_TSL210
Python Script for digitally controlling the Santec_TSL210 Laser using pyserial via the RS232-C connection

PySerial must be installed in order for this to work.

The serial commands are found in the manual under section 10-8.

When running the laser, the first command after turning the laser on must be LO. This turns on the injection current of the laser. You will see the LD LED turn on signifying that the laser is working. The last command before turning the laser off must be LF. This turns the current injection off. Wait until the LD LED turns off and then it is safe to power off the laser. 
