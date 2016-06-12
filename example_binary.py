import lumos

for i in xrange(240):
	bina = format(i, 'b')[::-1]
	#print(bina)
	bina = bina.replace('0','000000')
	bina = bina.replace('1','aaaaaa')
	#print(bina)
	lumos.push(bina)
