import serial
import binascii
ser = serial.Serial('/dev/cu.usbserial-TG1101910', 9600)

# Read line   
while True:
    b = ser.read(1)
    print(binascii.hexlify(b))
