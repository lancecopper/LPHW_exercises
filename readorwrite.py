#! /urs/bin/env python

'read&write.py--user to choose create a new text file or read an existed one'

import os

ls = os.linesep
flag=0

while flag not in ['1','2']:   
    flag=raw_input("to choose: [1]create; [2]read >" )
    
if flag=='1':
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
    
elif flag=='2':
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

else:
    print("unexpected error: unexpected choice")
   