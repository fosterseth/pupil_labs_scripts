import numpy
import sys

timestamps = numpy.fromfile(sys.argv[1], dtype='>f8')
timestamps.tofile(sys.argv[2], "\n", "%f")



'''import struct
# http://stackoverflow.com/questions/30124608/convert-unsigned-integer-to-float-in-python
while True:
    x = struct.unpack('>I', f.read(4))
    if x == '':
        break
    y = struct.pack('>l', x[0])
    z = struct.unpack('>f', y)
    fout.write("%f\n" % z[0])'''