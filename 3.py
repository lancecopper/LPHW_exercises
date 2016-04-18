#! /urs/bin/env python

'makeTextFile.py--create text file'

ls = os.linesep

#get filename
while True:
    fname=raw_input('input filename> ')
    try:
        fobj=open(fname, 'w')
    except IOError, e:
        print "*** file open error:", e
    else:
        break
    
   
#get file content (text) linesep
all=[]
print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry=raw_input('say something> ')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj.writelines(['%s%s' %(x, ls) for x in all])
fobj.close()
print 'DONE!'