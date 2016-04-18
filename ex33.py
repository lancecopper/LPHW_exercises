from sys import argv
script, argv1, argv2 = argv

def add_number(a, b):
    a = int(a)
    b = int(b)
    i = 0
    numbers = []
    
    while i < a:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + b
        print "Numbers now: ", numbers
        print "At the bottom i is %d" %i
	
    print "The numbers: "

    for num in numbers:
        print num
		
add_number(argv1, argv2)