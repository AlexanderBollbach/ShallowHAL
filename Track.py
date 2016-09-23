import numpy as np
import scipy.io.wavfile as wavfile
from Bpm1 import get_file_bpm
from DSP import getAudioBand
from utilities import *
from AudioToSeqCode import *

from OnsetType import OnsetType


class Track(object):
    def __init__(self, name, filepath):

        self.name = name
        self.filepath = filepath
        self.get_audio()

        self.filterFirst()

        self.onsets = self.init_onsets()

        freqs = []
        # for onset in self.onsets:
            # freqs.append(primary_freq_from_onset(self.audio, onset))

        # self.onsets = zip(self.onsets, freqs)
        # self.quantizeFreqs()
        # self.colorize()

        self.getSixteenth()

        for i in range(len(self.onsets)):
            self.onsets[i].sample = reduceSamplesDuration(self.onsets[i].samples, self.sixteenthNote)


        deltas = []
        for i in range(len(self.onsets)):
            if i == 0:
                deltas.append(self.onsets[i].sample)
                continue

            deltas.append(self.onsets[i].sample - self.onsets[i - 1].sample)

        for i in range(len(deltas)):


            base = 5
            delta = int(base * round(float(deltas[i]) / base))
            self.onsets[i].delta = delta / self.sixteenthNote






        self.seq = self.seq_from_deltas()

        print self.onsets




    def colorize(self):

        for i in range(len(self.onsets)):

            cur = self.onsets[i][1]
            c = ''
            if cur < 100:
                c = 'red'
            elif cur > 100 and cur < 200:
                c = 'green'
            else:
                c = 'blue'

            self.onsets[i] += (c,)

    def get_audio(self):
        rate, audio = wavfile.read(self.filepath)
        audio = np.asarray(audio, dtype=np.double)
        audio /= np.max(audio)

        self.audio = audio
        self.rate = rate

    def getSixteenth(self):
        bpm = get_file_bpm(self.filepath)
        bpm = float(bpm)

        beatsPerSec = float(bpm) / 60
        numSamplesPerBeat = self.rate / beatsPerSec

        numSamplesPer16th = numSamplesPerBeat / 4
        numSamplesInThous = round(numSamplesPer16th, -3)
        numSamplesAsOne = numSamplesInThous / 1000

        self.sixteenthNote = numSamplesAsOne

    def get_banded_seq_code(self, range):
        banded_audio = getAudioBand(self.audio, range)
        code = seq_from_audio(banded_audio)
        return code

    def quantizeFreqs(self):

        for onset in self.onsets:
            print onset

    def filterFirst(self):
        self.audio = getAudioBand(self.audio, [80, 800])

    def init_onsets(self, sampling_rate=44100):

        odf = modal.ComplexODF()

        odf.set_hop_size(512)

        odf.set_frame_size(1024)
        odf.set_sampling_rate(sampling_rate)
        odf_values = np.zeros(len(self.audio) / 512, dtype=np.double)
        odf.process(self.audio, odf_values)
        onset_det = od.OnsetDetection()
        onset_det.peak_size = 30
        onsets = onset_det.find_onsets(odf_values) * odf.get_hop_size()


        onsets_arr = []

        for onset in onsets:
            on_cur = OnsetType()
            on_cur.samples = onset
            onsets_arr.append(on_cur)

        return onsets_arr



    def seq_from_deltas(self):

        noteOns = []

        for i in range(len(self.onsets)):
            noteOns.append(1)
            for _ in range(int(self.onsets[i].delta) - 1):
                noteOns.append(0)

        return noteOns



    def printSeqCode(self):

        import sys

        for code in self.seq:



            if code == 1:
                sys.stdout.write(u'\u25A0')
                sys.stdout.write(' ')
            else:
                sys.stdout.write(u'\u25A1')
                sys.stdout.write(' ')



        print ""


#
#
# def primary_freq_from_onset(self, onset, fft_size=8192):
#
#     if onset + fft_size > len(self.audio) :
#         return -1
#
#
#     slice = self.audio[onset: onset + fft_size]
#     fft_results = abs(fft(slice))
#     T = (1. / 44100) * fft_size
#     df = 1 / T
#     freqs = np.fft.fftfreq(fft_size) * fft_size * df
#
#     both = zip(fft_results, freqs)
#
#     # both = both[0:80]
#
#
#
#     a_max = np.argmax(both, axis=0)
#
#     result = freqs[a_max[0]]
#     result = round(result, -1)
#     return result
#



def reduceSamplesDuration(samplesInterval, sixteenthNote=6):
    a = samplesInterval
    a = round(a, -2)
    a /= 1000
    a = int(a)
    # a /= sixteenthNote
    return a


