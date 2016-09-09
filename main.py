from utilities import *

from PatternMatcher import PatternMatcher
from Track import Track

track = Track("testSample1", "audio/kicksnare7.wav")





print track.onsets


one_onset = track.audio[track.onsets[5]:track.onsets[5] + 8192]



from scipy.fftpack import fft

fft = fft(one_onset)

from matplotlib import pyplot as plt

plt.figure(1,figsize=(30,10))




plt.subplot(211)
plt.title("onsets")
plt.plot(track.audio)
for onset in track.onsets:
    plt.axvline(x=onset,linewidth=2, color='r')


plt.subplot(212)

plt.plot(one_onset)

plt.show()





exit(0)





matcher = PatternMatcher(track)
matcher.pattern = [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]


maxBand = matcher.findPattern()




print "maxband: " + str(maxBand)




#
#
#


band_range1 = [400,450]
band_range2 = [1000,1050]


seq_band1 = track.get_banded_seq_code(band_range1)
seq_band2 = track.get_banded_seq_code(band_range2)

printSeqCode(seq_band1)
printSeqCode(seq_band2)




from DSP import getAudioBand

audioband1 = getAudioBand(track.audio, band_range1)
audioband2 = getAudioBand(track.audio, band_range2)


from scipy.io import wavfile

wavfile.write('audio/band1.wav',44100,audioband1)
wavfile.write('audio/band2.wav',44100,audioband2)












from AudioToSeqCode import onsets_from_audio

onsets1 = onsets_from_audio(audioband1)
onsets2 = onsets_from_audio(audioband2)


from matplotlib import pyplot as plt

plt.figure(1,figsize=(30,10))



plt.subplot(211)
plt.title("band 400-450hz")
plt.plot(audioband1)
for onset in onsets1:
    plt.axvline(x=onset,linewidth=2, color='r')




plt.subplot(212)
plt.title("band 1000-1050hz")
plt.plot(audioband2)
for onset in onsets2:
    plt.axvline(x=onset,linewidth=2, color='r')




plt.show()















