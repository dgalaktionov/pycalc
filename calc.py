#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import *
from sys import argv, stdin, stdout
from tty import setraw, setcbreak
from threading import Thread

DEBUG=False

class EscapeThread(Thread):
	def __init__(self, *args, **kwargs):
		Thread.__init__(self, daemon=True, *args, **kwargs)

	def run(self):
		stdin.read(1)

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
	cursor = 0
	while True:
		c = stdin.read(1)[0]
		co = ord(c)
		if co in [3,4]: # CTRL+C, CTRL+D
			break
		elif co == 27: # ESC
			# It could be an escape or the start of an arrow key
			# Depends on the next bytes, if there are any
			t = EscapeThread()
			t.start()
			t.join(0)

			if t.is_alive():
				# If it's a real escape, exit
				break
		elif co == 68: # LEFT ARROW
			cursor -= 1
		elif co == 67: # RIGHT ARROW
			cursor += 1
		elif co == 13: # ENTER
			stdout.write("\n\r")
			calculate(a)
			a = ""
			cursor = 0
		elif co == 127: # BACKSPACE
			if cursor > 0:
				a = a[:cursor-1] + a[cursor:]
				cursor -= 1
		elif co == 126: # DEL
			# In UNIX it's actually 2 byes that we have to remove
			a = a[:cursor-1] + a[cursor+1:]
			cursor -= 1
		elif co == 72: # HOME
			cursor = 0
		elif co == 70: # END
			cursor = len(a)
		else:
			a = a[:cursor] + c + a[cursor:]
			cursor += 1

		if cursor < 0:
			cursor = 0
		if cursor > len(a):
			cursor = len(a)

		stdout.write("\r")
		stdout.write(" " * (len(a)+6))
		stdout.write("\r")
		stdout.write(">>> ")
		if DEBUG:
			stdout.write(str(list(map(ord,a))))
		else:
			stdout.write(a)
			stdout.write("\r")
			stdout.write(">>> ")
			stdout.write(a[:cursor])
		stdout.flush()

	stdout.write("\r\n")
	stdout.flush()
