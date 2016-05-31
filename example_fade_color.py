import lumos

color = 'FF00FF'
while color != '000000':
	lumos.push(color,1)
	color = lumos.pixel_brightness(color,-10)
	print(color)


lumos.push(color,1)

