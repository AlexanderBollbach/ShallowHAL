#! /usr/bin/env python

from aubio import source, onset


def getOnsets(filename, samplerate=44100):


    win_s = 512  # fft size
    hop_s = win_s // 2  # hop size




    s = source(filename, samplerate, hop_s)



    samplerate = s.samplerate

    o = onset("default", win_s, hop_s, samplerate)

    # list of onsets, in samples
    onsets = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        if o(samples):
            # print("%f" % o.get_last_s())
            onsets.append(o.get_last())
        total_frames += read
        if read < hop_s: break

    return onsets
