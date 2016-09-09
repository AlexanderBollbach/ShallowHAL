from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, band_range, fs=44100, order=2):

    low = band_range[0]
    high = band_range[1]
    b, a = butter_bandpass(low, high, fs, order=order)
    y = lfilter(b, a, data)
    # y *= 0.0001
    return y




def getAudioBand(audio,band_range):
    return butter_bandpass_filter(audio,band_range)