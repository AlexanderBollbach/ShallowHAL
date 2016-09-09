
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def getCompsFromAudio(file):
    fs, data = wavfile.read(file)  # load the data
    s = np.fft.fft(data) / len(data)  # take the fft and normalize
    s = s[range(len(data) / 2)]  # one-sided frequency range
    freq = [i for i in range(0, len(data) / 2)]  # generate frequencies

    return freq, abs(s)



freq_kick, s_kick = getCompsFromAudio('kick1.wav')
freq_snare, s_snare = getCompsFromAudio('snare1.wav')



plt.figure(1)
plt.subplot(211)
plt.xlim([0,500])
plt.ylim([0,5000])

plt.plot(freq_kick, s_kick)

plt.subplot(212)
plt.xlim([0,1000])
plt.ylim([0,5000])

plt.plot(freq_snare, s_snare)
plt.show()