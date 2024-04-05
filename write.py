import serial
import binascii
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)

#Written in 45 mins, super ammounts of errors, do not use like all other good Github code

# b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'01' b'aa' 
# b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'02' b'11' b'98' 
# b'53' b'4e' b'44' b'4e' b'21' b'14' b'00' b'03' b'11' b'01' b'00' b'10' b'73' 
# b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'04' b'10' b'14' b'00' b'11' b'72' 

id11 = hex(1) #set this in code
id12 = hex(0) #set this in code
thing1 = hex(11) #set this in code

id21 = hex(0) #read this from serial
id22 = hex(0) #read this from serial
thing2 = hex(2) #read this from serial

#Send Msg 1
# b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'01' b'aa' 
# SNDN!+ID(01/00)+THING#(1)+CRC(aa)
ser.write(b'SNDN!')
ser.write(id11)
ser.write(id12)
ser.write(hex(1))

# COMPUTE CRC and write to serial
ser.write('aa') ##this shouldnt be aa im just fat fingering it until we actually compute CRC

while True:
    result = ser.read(1)
    if(result == b'S'):
        print("")
        break
    print(binascii.hexlify(result), end=" ")
    ser.write(b'SNDN!')

#Send Msg 2
# b'53' b'4e' b'44' b'4e' b'21'   b'01' b'00'    b'02'      b'11'       b'98' 
# SNDN!                         + ID1(01/00)   + MSG#(2)  + THING1(11) + CRC
# Compute CRC based on ID
# Send to target badge

#Recv Msg 3 and Process - Compute CRC
# b'53' b'4e' b'44' b'4e' b'21'   b'14' b'00'    b'03'      b'11'        b'01' b'00'   b'10'    b'73' 
# SNDN!                         + ID2(14/00)   + MSG#(3)  + THING1(07) + ID1(01/100) + THING2 + CRC

#Send Msg 4 and Process
# b'53' b'4e' b'44' b'4e' b'21'   b'01' b'00'    b'04'      b'10'        b'14' b'00'   b'11'    b'72' 
# SNDN!                         + ID1(01/00)   + MSG#(4)  + THING2(10) + ID2(01/100) + THING1 + CRC
