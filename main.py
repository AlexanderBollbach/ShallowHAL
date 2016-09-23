from utilities import *
from scipy.fftpack import fft, fftfreq
import numpy as np
from PatternMatcher import PatternMatcher
from Track import Track

track = Track("testSample1", "audio/8bars.wav")

track.printSeqCode()









#
# from matplotlib import pyplot as plt
#
# plt.figure(1, figsize=(30, 15))
#
# data_onsets = [i.sample for i in track.onsets]
# data_freqs = [i.freq for i in track.onsets]
#
# data_colors = [ch[2] for ch in track.onsets]
#
# max_freqs = np.amax(data_freqs)
# new_max = 1
#
# data_freqs = [(float(x) / max_freqs) * new_max for x in data_freqs]
#
# plt.scatter(data_onsets, data_freqs, color=data_colors)
#
# plt.plot(track.audio, color='y', zorder=0)
#
# plt.ylim([-1, 1])

# plt.show()



#
#
