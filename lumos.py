import time
from collections import Counter

config_length = 1024					#Defining led array
config_length_hex = (config_length*6)
config_brightness=-1
config_error=[]
config_error_time=(int(time.time())+10)


def console(frame):
	#Function keeps track of occurring errors, displaying them every 10 seconds..
        global config_error,config_error_time
        config_error.append(frame)
        if config_error_time<int(time.time()):
                counts = Counter(config_error)
                print(counts)
                config_error=[]
                config_error_time=(int(time.time())+10)

try:
        import serial
        port = "/dev/teensy"				#Defining our serial port
        usart = serial.Serial (port,921600)
except:
        console('Serial module fail')


def push(frame='',repeat=False):			#Main function, send frame to the Teensy
	global config_length_hex,config_brightness
	while len(frame)<config_length_hex:		#We do need a full frame
		if(repeat and len(frame)>0):		#Repeat...
			frame += frame
		else:					#or fill with zeros
			frame += '000000000000000000'
	if len(frame) % 2:   				#Hex frames shouldn't be odd-length
		frame += '0'
     
	frame_hex = '01'				#needed to announce start of frame
	frame_hex += frame[:config_length_hex]
	frame_bytes = frame_hex.decode("hex")
	console("Frame pushed")
        try:
                usart.write(frame_bytes)			
        except:
                console('Serial connection fail')
	

def clear():						#Send an empty frame
	push('000000',1)

def master_brightness(offset):
        if offset>-256 and offset<256:
                config_brightness=offset

def brightness(frame,offset=-1): 		            #takes a color like 87c95f and produces a lighter or darker variant
   pixels=[]
   new_rgb = []			
   pixels = [frame[x:x+6] for x in range(0,len(frame),6)]
   for hex_color in pixels:
    if len(hex_color) != 6:
        console("Wrong format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [0, 2, 4]]
    new_rgb_int = [(int(hex_value, 16)*(100+offset))/100 for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] #make sure new values are between 0 and 255
    new_rgb = []
    for i in new_rgb_int:
        i=hex(i)[2:]
        if len(i)<2:
            i = '0'+i
	new_rgb.append(i)
    return "".join([i for i in new_rgb])[:config_length_hex]
