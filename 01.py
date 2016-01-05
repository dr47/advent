
import sys

floor=0

for c in sys.stdin.read():
	if c == '(':
	    floor += 1
	elif c == ')':
	    floor -= 1
print floor
