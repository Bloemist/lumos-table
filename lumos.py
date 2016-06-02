import serial
import time
port = "/dev/teensy"					#Defining our serial port
usart = serial.Serial (port,115200)
leds = 144						#Defining led array
leds_hex = (leds*6)
brightness=0
def push(frame='',repeat=False):			#Main function, send frame to the Teensy
	
	message_hex = frame
	while len(message_hex)<leds_hex:		#We do need a full frame
		if(repeat and len(frame)>0):		#Repeat...
			message_hex += frame
		else:					#or fill with zeros
			message_hex += '0'
	if len(message_hex) % 2:   			#Hex messages shouldn't be odd-length
		message_hex += '0'
	n = 6						#reducing brightness for each pixel				
	pixels = [pixel_brightness(message_hex[i:i+n],brightness) for i in range(0, len(message_hex), n)]
	message_hex = '01'				#needed to announce start of frame
	message_hex += "".join([i for i in pixels])
	message_bytes = message_hex.decode("hex")
	usart.write(message_bytes)
	#print(message_hex)				#for debugging?

def clear():						#Send an empty frame
	push('000000',1)


def pixel_brightness(hex_color, brightness_offset=1):
    """ takes a color like 87c95f and produces a lighter or darker variant """
    if len(hex_color) != 6:
        raise Exception("Wrong format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [0, 2, 4]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] #make sure new values are between 0 and 255
    new_rgb = []
    for i in new_rgb_int:
        i=hex(i)[2:]
        if len(i)<2:
            i = '0'+i
	new_rgb.append(i)
    return "".join([i for i in new_rgb])	
