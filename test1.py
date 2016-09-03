import numpy

import scipy.io.wavfile

import sys

file = sys.argv[1]


eachBeatGets = 44100 / 2.26619 * 4



rate, data = scipy.io.wavfile.read(file)

print rate


for i in range(len(data)):

   if i % eachBeatGets > eachBeatGets - 15000:
      data[i] = 0


scipy.io.wavfile.write('test.wav',rate,data)
