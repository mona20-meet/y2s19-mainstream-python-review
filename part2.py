# Part 2 of the Python Review lab.
def prime(x):
	for i in range(2,x):
		if (x % i) == 0:
			print(x,"is not a prime number")
			break

		else:
			print(x,"is a prime number")
			break



def encode(x, y):
	prime(x)
	if 1 < y < 250 and 500 < x < 1000 :

		return(x*y)
	else:
		print ('Invalid input: Outside range.')

	


def decode(coded_message):
	pass