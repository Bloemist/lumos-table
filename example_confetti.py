import lumos,random,time
i=0
frame=''
while i<144:
	frame += '000000'	
	i = i+1
line = frame
pixels = [line[i:i+6] for i in range(0, len(line), 6)]
new_pixels=[]
frame = line
while True:
	new_pixels = []
	lumos.push(frame,1)
	for i in pixels:
		new_pixels.append(lumos.brightness(i,-4))
		
	frame = "".join([i for i in new_pixels])
	pixels = new_pixels
	r = lambda: random.randint(0,255)
	color = ('%02X%02X%02X' % (r(),r(),r()))
	pixels[random.randint(0,140)] = color
	pixels[random.randint(0,140)] = color
