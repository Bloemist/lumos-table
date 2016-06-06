import lumos,random
i=0
line=''
while i<144:
	line += '000000'	
	i = i+1
n = 6
pixels = [line[i:i+n] for i in range(0, len(line), n)]
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
	index = random.randint(0,140)
	pixels[random.randint(0,140)] = color
	pixels[index] = color
lumos.push(color,1)

