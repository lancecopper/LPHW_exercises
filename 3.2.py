#! /urs/bin/env python

'readTextFile.py--read and display text file'

import os

#get filename
fname = raw_input('Enter filename: ')
print

#attempt to open file for reading

if os.path.exists(fname):
    fobj = open(fname, 'r')
    for eachLine in fobj:
        print eachLine.strip()
    fobj.close()
else:
    print "ERROR: '%s' doesn't exists" % fname
   

