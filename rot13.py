#!/usr/bin/env python2.6
# Info: Script will decode rot 13

import string
import sys

from os.path import basename

if len(sys.argv) != 2:
    print 'Usage: %s text' % basename(sys.argv[0])
    sys.exit(1)

print sys.argv[1].decode('rot13')
