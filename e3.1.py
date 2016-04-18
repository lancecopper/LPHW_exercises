#!/sur/bin/env python

"""makeTextFile.py -- create text file """

import os
# linesep can help to add different line break mark in different os 
ls = os.linesep

# get filename
fname = raw_input("filename?\n > ")

while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break
        
        
# get file content (text) linesep
all = []
print "\nEnter lines('.'by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)
        
# write lines to file with proper line-ending
# open--this instruction can create a new file!!!
fobj = open(fname, 'w')


fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'
