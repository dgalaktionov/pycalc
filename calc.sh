#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 $DIR/calc.py "$@"
stty sane
