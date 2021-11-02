from dis import dis
def func():
	f = ''
	a = 'rwhxi}eomr\\^`Y'
	z = 'f]XdThbQd^TYL&\x13g'

	a += z

	for i, b in enumerate(a):
		c = ord(b)
		c -= 7
		c += i
		c = chr(c)
		f += c
	print(f)

func()

# dis(func)
