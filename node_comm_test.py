#UART Pins on the BeagleBone are on: P9.24 (txd) and P9.26 (rxd)
#This utilizes ttyO1 serial port on BBBW
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import binascii


#Setup UART1 and P8_10 as the RTS pin for RS485 Communication
UART.setup("UART1")
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.LOW)   # Places RS485 Breakout chip in Re$
GPIO.output("P8_10", GPIO.HIGH)  # Paces RS485 Breakout chip in Tra$



loopValue = 0

# Add a test loop with delay here:

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()

# ##
# Write the message to the node:
# ##

ser.open()

if ser.isOpen():
    print "Serial is open, port name is: " + ser.name
    print "Print settings are: "
    print ser


    # Loop and print things to see if it transmits.
    while(loopValue < 1):

       print "We made it " + str(loopValue)
       # ser.write(" Testing RS232-RS485 Transmission\n\r")

       # cmd_string='3a010001ff0d0a'
       # cmd_string = bytes([0x3a,0x01,0x00,0x01,0xff,0x0d,0x0a]);
       # ser.write(cmd_string.decode("hex"))

       # cmd_bytes = bytearray.fromhex(cmd_string)
       # ser.write("\x3a\x01\x00\x01\xff\x0d\x0a\n\r")


       #  Print the cmd_string in hex version:
       #  for cmd_byte in cmd_bytes:
       #  hex_byte = ("{0:02x}".format(cmd_byte))
       #  print (hex_byte)
       #  ser.write(bytearray.fromhex(hex_byte))
       #  time.sleep(.100)

       # Try Creating and sending a packet:

     #  packet = bytearray([0x3a,0x01,0x00,0x01,0xff,0x0d,0x0a])
       #ser.write(str(packet))

       #byte = chr(0x3a)
       #ser.write(byte)
       #byte2 = '\x3a'
       #ser.write(byte2)

       #  ser.write('0x3a')
     #  ser.write('0x01')
     #  ser.write('0x00')
     #  ser.write('0x01')
     #  ser.write('0xff')
     #  ser.write('0x0d')
     #  ser.write('0x0a')

     #  ser.write('\n\r')
     #  ser.write('\n\r')


###
# Method 1
###
       command_string = "3a010001ff0d0a".decode("hex")
       ser.write(command_string)

        #ser.write('3a')
       #ser.write('01')
       #ser.write('00')
       #ser.write('01')
       #ser.write('ff')
       #ser.write('0d')
       #ser.write('0a')

      # ser.write('\n\r\n\r')


###
# Method 2
###
     # command_string = "3a010001ff0d0a".decode("hex")
     # ser.write(command_string)

     #  ser.write('\n\r')

      #  ser.write('\n\r')
     #  ser.write(b'\x3a\x01\x00\x01\xff\x0d\x0a')
     #  ser.write('\n\r')
     #  ser.write('\n\r')


       #print str(packet)
       #packet.append(0x3a)
       #packet.append(0x01)
       #packet.append(0x00)
       #packet.append(0x01)
       # ser.write(packet + '\r\n')
       #ser.write(cmd_string)

       loopValueString = str(loopValue)

       #ser.write(loopValueString)
       ser.write('\n\r')
        #time.sleep(2)
       loopValue = loopValue + 1

#ser.write("\n\n\r\r")
#ser.write("Read Mode: ")
#ser.write("\n\n\r\r")
ser.close()

# ##
# Read back the message from the node:
# ##

GPIO.output("P8_10", GPIO.LOW)   # Places RS485 Breakout chip in Re$

ser.open()

if ser.isOpen():
    print "Serial is open, port name is: " + ser.name
    print "Print settings are: "
    print ser

    while True:
      line = ser.read()
      print line.encode('hex')

ser.close()

# Eventually, you'll want to clean up, but leave this commented for$
# as it doesn't work yet
#UART.cleanup()






