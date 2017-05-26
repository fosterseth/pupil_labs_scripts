import numpy, sys

x = numpy.fromfile(sys.argv[1], dtype='>f8')
numpy.save(sys.argv[2], x)