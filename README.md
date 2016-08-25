# pycalc
CLI calculator tool based on Python 3

I made it because of my frustration with bc and other similar tools, when all I wanted was a handy but powerful shell calculator.
Won't work on Windows.


##Usage:

`$ python3 calc.py 'log2(4)'`

Outputs: 

2.0


`$ python3 calc.py 2+2 2**3`

Outputs:

4

8


`$ python3 calc.py`

With no arguments, invokes an interactive shell. ESC, CTRL+C or CTRL+D to exit. It's recommended to call the shell through calc.sh to fix the tty after quitting.


If you are going to use it often like me, make an alias in your .bashrc or whatever your shell is, like `alias c='bash /home/dgalaktionov/calc.sh'`
