import serial
import binascii
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
while True:
    result = ser.read(1)
    if(result == b'S'):
        print("")
    print(binascii.hexlify(result), end=" ")
    
#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'01' b'aa' 
#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'02' b'07' b'a2' 
#b'53' b'4e' b'44' b'4e' b'21' b'14' b'00' b'03' b'07' b'01' b'00' b'11' b'7c' 
#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'04' b'11' b'14' b'00' b'07' b'7b' 

#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'01' b'aa' 
#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'02' b'11' b'98' 
#b'53' b'4e' b'44' b'4e' b'21' b'36' b'00' b'03' b'11' b'01' b'00' b'10' b'51' 
#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'04' b'10' b'36' b'00' b'11' b'50' 

#b'53' b'4e' b'44' b'4e' b'21' b'01' b'00' b'01' b'aa' 
#b'53' b'4e' b'44' b'4e' b'21' b'36' b'00' b'02' b'11' b'63' 
#b'53' b'4e' b'44' b'4e' b'21' b'14' b'00' b'03' b'11' b'36' b'00' b'10' b'3e' 
#b'53' b'4e' b'44' b'4e' b'21' b'36' b'00' b'04' b'10' b'14' b'00' b'11' b'3d' 
