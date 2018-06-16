#!/usr/bin/env python2.6
# Info: Script will decode rot 13

import string
import sys

from os.path import basename

if len(sys.argv) != 2:
    print 'Usage: %s textfile' % basename(sys.argv[0])
    sys.exit(1)

filepath=sys.argv[1]
file = open(filepath, "r")
text=text.read()
print a.decode('rot13')
