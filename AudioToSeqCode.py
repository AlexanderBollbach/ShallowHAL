from scipy.io import wavfile
import numpy as np
from DSP import getAudioBand

import modal
import modal.onsetdetection as od

def reduceSamplesDuration(samplesInterval, sixteenthNote=6):
    a = samplesInterval
    a = round(a, -2)
    a /= 1000
    a = int(a)
    a /= sixteenthNote
    return a







def onsets_from_audio(audio, sampling_rate=44100):

    odf = modal.ComplexODF()
    odf.set_hop_size(512)
    odf.set_frame_size(2048)
    odf.set_sampling_rate(sampling_rate)
    odf_values = np.zeros(len(audio) / 512, dtype=np.double)
    odf.process(audio, odf_values)
    onset_det = od.OnsetDetection()
    onset_det.peak_size = 3
    onsets = onset_det.find_onsets(odf_values) * odf.get_hop_size()

    return onsets


def seq_from_audio(audio, sampling_rate=44100):



    onsets = onsets_from_audio(audio)

    # for onset in onsets:
    last = 0
    for i, onset in enumerate(onsets):
        a = onset - last
        a = reduceSamplesDuration(a)
        last = onset
        onsets[i] = a

    # trim beginning weirdness
    final_deltas = np.delete(onsets, [0, 1, 3])

    noteOns = []

    for onset in final_deltas:
        noteOns.append(1)
        for i in range(onset - 1):
            noteOns.append(0)

    return noteOns









def seq_from_band(audio, range, sampling_rate=44100):


    audio = getAudioBand(audio, range)

    return seq_from_audio(audio)



