from AudioToSeqCode import getSeqCodeFromBand
from Track import *

import math



class PatternMatcher(object):




    def __init__(self, track):
        self.track = track
        self.pattern = None



    def match16(self, seqCodeSlice):

        score = 0
        for i in range(0,16):
            if seqCodeSlice[i] == self.pattern[i]:
                score += 1
        return score




    def findPattern(self):



        cutoff = 0
        scoreForBands = {}

        while cutoff < 5000:

            seqCode = getSeqCodeFromBand(self.track.audio, [cutoff, cutoff + 50])

            scoreForBands[cutoff] = 0

            numBars = int(math.floor(len(seqCode) / 16))

            curScore = 0

            for i in range(numBars):
                pointInArray = i * 16
                seqCodeSlice = seqCode[pointInArray:pointInArray+16]
                curScore += self.match16(seqCodeSlice)


            scoreForBands[cutoff] = curScore


            print "band: " + str(cutoff) + "score: " + str(curScore)

            cutoff += 50


        minVal = 1000000
        maxVal = 0
        for band, score in scoreForBands.iteritems():
            if score > maxVal:
                maxVal = score
            if score < minVal:
                minVal = score

        for band, score in scoreForBands.iteritems():
            normalized = float(score - minVal) / (maxVal - minVal)
            scoreForBands[band] = normalized

        for band, score in sorted(scoreForBands.iteritems()):
            print "band: " + str(band) + "score: " + str(score)

        maxScore = 0
        maxBand = 0
        for band, score in scoreForBands.iteritems():
            if score > maxScore:
                maxScore = score
                maxBand = band

        return maxBand
