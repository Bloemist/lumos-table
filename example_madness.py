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
	pixels = []
	i=0
	while i<144:
		pixels.append('000000')
		i = i+1
	r = lambda: random.randint(0,255)
	color = ('%02X%02X%02X' % (r(),r(),r()))
	pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	#pixels[random.randint(0,140)] = color
	pixels[random.randint(0,140)] = color


	frame = "".join([i for i in pixels])
	lumos.push(frame,1)






lumos.push(color,1)

