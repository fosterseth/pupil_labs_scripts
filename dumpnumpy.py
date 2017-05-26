import numpy
import sys

data = numpy.load(sys.argv[1])
fout = open(sys.argv[2], 'w')
for d in data:
    fout.write('%f\n' % d)
    
fout.close()