import numpy as np

import scipy.io.wavfile as wavfile









def printSeqCode(seqCode):
    import sys

    for code in seqCode:
        if code == 1:
            sys.stdout.write(u'\u25A0')
            sys.stdout.write(' ')
        else:
            sys.stdout.write(u'\u25A1')
            sys.stdout.write(' ')

    print ""
























