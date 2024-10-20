## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	r = int("0")
	i = int("1")
	while i <= x:
		if x % i == 0:
			r = r + int("1")
		i = i + int("1")

	l = x - int("1")
	s = 0

	while l >= int("1") and s < r:
		a = int("1")
		s = 0
		while a <= l:
			if l % a == 0:
				s = s + int("1")
			a = a + int ("1")
		l = l - int("1")


	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	if s < r:
		res = ("anti-prime")
	else:
		res = ("not anti-prime")
	return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	import sys
	x = int (sys.argv [1])
	print(main(x))
