#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import *
from sys import argv, stdin, stdout
from tty import setraw, setcbreak

def calculate(a):
	try:
		print(eval(a))
	except (NameError, ValueError, SyntaxError, ArithmeticError):
		pass

if len(argv) > 1:
	for a in argv[1:]:
		calculate(a)
else:
	setraw(stdin)
	stdout.write(">>> ")
	stdout.flush()
	a = ""
	while True:
		c = stdin.read(1)[0]
		co = ord(c)
		if co in [3,4,27]:
			break

		if co == 13:
			stdout.write("\n\r")
			calculate(a)
			a = ""
		elif co == 127:
			a = a[:-1]
		else:
			a += c

		stdout.write("\r")
		stdout.write(" " * (len(a)+5))
		stdout.write("\r")
		stdout.write(">>> ")
		stdout.write(a)
		stdout.flush()

	stdout.write("\n\r")
	stdout.flush()
