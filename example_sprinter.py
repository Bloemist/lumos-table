import lumos,random,time
i=0
line=''
while i<144:
        line += '000000'
        i = i+1
pixels = [line[i:i+6] for i in range(0, len(line), 6)]
new_pixels=[]
frame = line
l=0
r=True
while True:
        new_pixels=[]
	if l>130:
		b=False
	if l<5:
		b=True
	if b:
		l=l+1
	if b==False:
		l=l-1
        #print(l)
	lumos.push(frame)
        for i in pixels:
                new_pixels.append(lumos.brightness(i,-16))
        frame = "".join([i for i in new_pixels])
        pixels = new_pixels
        r = lambda: random.randint(5,255)
        color = ('%02X%02X%02X' % (r(),r(),r()))

	pixels[l]=color









