import lumos

for i in xrange(1024):
	bina = format(i, 'b')[::-1]
	#print(bina)
	bina = bina.replace('0','000000')
	bina = bina.replace('1','FFFFFF')
	#print(bina)
	lumos.push(bina)
