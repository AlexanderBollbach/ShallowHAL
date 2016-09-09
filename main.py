from utilities import *

from PatternMatcher import PatternMatcher
from Track import Track

track = Track("testSample1", "audio/kicksnare6.wav")


matcher = PatternMatcher(track)
matcher.pattern = [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]


# maxBand = matcher.findPattern()



band1 = track.get_banded_seq_code([650,700])
band2 = track.get_banded_seq_code([2500,2550])


printSeqCode(band1)
printSeqCode(band2)



from DSP import getAudioBand

audioband1 = getAudioBand(track.audio, [650,700])
audioband2 = getAudioBand(track.audio, [2500,2550])


from scipy.io import wavfile

wavfile.write('audio/band1.wav',44100,audioband1)
wavfile.write('audio/band2.wav',44100,audioband2)


























# wavfile.write("audio/filtered2.wav", 44100, audio)













# audio[last:onset] = butter_bandpass_filter(audio[last:onset], 0, highBound)


# plot onset detection results




# plt.plot(audio)
# plt.show()


#
# fig = plt.figure(1, figsize=(12, 12))
# plt.subplot(3, 1, 1)
# plt.title('Onset detection with ' + odf.__class__.__name__)
# plt.plot(audio, '0.4')
# plt.subplot(3, 1, 2)
# trplot.plot_detection_function(onset_det.odf, hop_size)
# trplot.plot_detection_function(onset_det.threshold, hop_size, "green")
# plt.subplot(3, 1, 3)
# trplot.plot_onsets(onsets, 1.0)
# plt.plot(audio, '0.4')
# plt.show()