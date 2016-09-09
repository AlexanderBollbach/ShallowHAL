from AudioToSeqCode import seq_from_band
from Track import *

import math



class PatternMatcher(object):




    def __init__(self, track):
        self.track = track
        self.pattern = None




    def score_for_starting_idx(self, seq, idx):

        score = 0

        pattern_idx = 0
        for i in range(idx, len(seq)):

            if seq[i] == self.pattern[pattern_idx % 16]:
                score += 1

            pattern_idx += 1

        return score







    def score_from_band(self, band_range):

        seq = seq_from_band(self.track.audio, band_range)


        max_score = 0
        best_idx = 0

        for i in range(len(seq)):

            score_for_idx = self.score_for_starting_idx(seq, i)

            if score_for_idx > max_score:
                max_score = score_for_idx
                best_idx = i


        return max_score, best_idx








    def findPattern(self):

        scoreForBands = {}

        cutoff = 0
        while cutoff < 2000:
            scoreForBands[cutoff] = self.score_from_band([cutoff, cutoff + 50])
            cutoff += 50


        # normalize and return max
        minVal = 1000000
        maxVal = 0
        for band, score in scoreForBands.iteritems():
            if score[0] > maxVal:
                maxVal = score[0]
            if score < minVal:
                minVal = score[0]

        for band, score in scoreForBands.iteritems():
            normalized = float(score[0] - minVal) / (maxVal - minVal)
            scoreForBands[band] = normalized

        for band, score in sorted(scoreForBands.iteritems()):
            print "band: " + str(band) + "score: " + str(score[0])

        maxScore = 0
        maxBand = 0
        for band, score in scoreForBands.iteritems():
            if score[0] > maxScore:
                maxScore = score[0]
                maxBand = band

        return maxBand
