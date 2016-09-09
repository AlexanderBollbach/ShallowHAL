import numpy as np
import scipy.io.wavfile as wavfile
from Bpm1 import get_file_bpm
from DSP import getAudioBand
import utilities
from AudioToSeqCode import *

class Track(object):

    def __init__(self, name, filepath):

        self.name = name
        self.filepath = filepath

        self.get_audio()





    def get_audio(self):
        rate, audio = wavfile.read(self.filepath)
        audio = np.asarray(audio, dtype=np.double)
        audio /= np.max(audio)

        self.audio = audio
        self.rate = rate


    def getSixteenth(self):
        bpm = get_file_bpm(self.filepath)
        bpm = float(100)
        # print "bpm: " + str(bpm)


        beatsPerSec = bpm / 60
        numSamplesPerBeat = self.rate / beatsPerSec
        numSamplesPer16th = numSamplesPerBeat / 4
        self.sixteenthNote = 6


    def get_banded_seq_code(self, range):
        banded_audio = getAudioBand(self.audio, range)
        code = seqCodeFromAudio(self.audio)
        return code







