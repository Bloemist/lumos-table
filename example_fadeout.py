import lumos

color = 'FF00FF'
while color != '000000':
	lumos.push(color,1)
	color = lumos.brightness(color,-5)
	#print(color)


lumos.push(color,1)

