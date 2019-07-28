# Part 2 of the Python Review lab.
def prime(x):
	for i in range(2,x):
		if (x % i) == 0:
			print(x,"is not a prime number")
			return False
	return True



def encode(x, y):
	while not prime(x):
		x+=1
	while not prime(y):
		y+=1
	if 1 < y < 250 and 500 < x < 1000 :

		return(x*y)
	else:
		print ('Invalid input: Outside range.')
		return None
	


def decode(coded_message):
	for x in range(501,1000):
		if prime (x):
			y = (coded_message / x )
			if (coded_message% x) == 0:
				if prime(y) and 1< y < 250:
					return (x , y)



