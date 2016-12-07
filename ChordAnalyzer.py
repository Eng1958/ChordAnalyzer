#!/usr/bin/env python3
# vim: number tabstop=4 expandtab shiftwidth=4 softtabstop=4 autoindent textwidth=100

"""
ChordAnalzyer.py is a ool to show the basic chords and scales
to analyse jazz pieces
Copyright (C) 2016  Dieter Engemann <dieter@engemann.me>

"""
import argparse

ChordList = ("C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B" )
CircleOfFifth = ("C", "G", "D", "A", "E", "B", "F#", "C#", "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F")

MajorList = (("maj7",0), ("m7",2), ("m7",4) , ("maj7",5), ("7",7), ("m7",9), ("m7b5",11))
HarmonicMinorList = (("mmaj7",0), ("m7b5",2), ("maj7#5",3) , ("m7",5), ("7(b9)",7), ("maj7",8), ("dim7",11))
MelodicMinorList = (("mmaj7",0), ("m7",2), ("maj7#5",3) , ("7",5), ("7",7), ("m7b5",8), ("7b5",11))


def Scale(ChordIndex, sign, ScaleType):
    """ print the scale beginning from the root note form a scale

        
        Different type of scaleis can be used. 
        ChordIndex:     "root note" index of the scale
        sign:           sharp or flat scale; C-Major ist nothing
        ScaleType:      Major, HarmonicMinor etc.
    """

    clist = []
    nlist = []

    if (ScaleType == "Major"):
        ScaleList = MajorList
    if (ScaleType == "NaturalMinor"):
        ChordIndex = ChordIndex + 9
        ScaleList = MajorList
    if (ScaleType == "HarmonicMinor"):
        ChordIndex = ChordIndex + 9
        ScaleList = HarmonicMinorList
    if (ScaleType == "MelodicMinor"):
        ScaleList = MelodicMinorList
        ChordIndex = ChordIndex + 9

    for ChordType in ScaleList:
        
        chordBase = ChordList[(ChordType[1] + ChordIndex) % len(ChordList)]
        if ("/" in chordBase):
            c = (chordBase.split("/"))
            if (sign[0] == "#" or sign[0] == ""):
                chordBase = c[0]
            else:
                chordBase = c[1]
        nlist.append(chordBase)
        clist.append(chordBase + ChordType[0])

    str = "Key of %s %s (%s)" % (nlist[0], ScaleType, ' '.join(nlist))
    print(str)
    print("".ljust(len(str), '-'))

    str = "I        II       III      IV       V        VI       VII"
    print(str)

    for c in clist:
 #       print("%-9s" % c, end="")
        print("Test")

    print("\n\n")

    if (ScaleType == "Major"):
        MajorScale(clist)
    if (ScaleType == "NaturalMinor"):
        print(clist)
        HarmonicMinorScale(clist)
    if (ScaleType == "HarmonicMinor"):
        print(clist)
        HarmonicMinorScale(clist)
    if (ScaleType == "MelodicMinor"):
        MelodicMinorScale(clist)

    print("\n\n")


def check_key(key):
    """
        Ueberprueft, ob der uebergebene "key" eine gueltige Tonart ist.

        Gibt den Index fuer die Tonart-Liste zurueck (C=0, C#/Db=1, ...)

        Pure implementation of quick sort al10yygorithm in Python
        :param collection: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
    """

    index = 0

    # go through entire ChordList and look for match
    for chord in ChordList:
        if (len(chord) == 1):
            if (chord == key):
                return index 
        else:
            t = (chord.split("/"))
            if (t[0] == key or t[1] == key):
                return index

        index = index + 1

    return -1

def getSignOfKey(key):
    """
    Construct a new 'Foo' object.

    :param name: The name of foo
    :param age: The ageof foo
    :return: returns nothing

    """

    returnList = []

    for index, k in enumerate(CircleOfFifth):

        if (key == k):
            if index == 0:
                sign = ""
                nsign = index
            if index >0 and index <= 6:
                sign = "#"
                nsign = index
            if index > 6:
                countFlat = len(CircleOfFifth) - index
                sign = "b"
                nsign = countFlat

            returnList.append(sign)
            returnList.append(nsign)
            return returnList


def MajorScale(ChordList):

    print("%s minor is the relative minor of %s major." % (ChordList[5],
    ChordList[0]))

    print("II-V-I: %s %s %s" % (ChordList[1], ChordList[4], ChordList[0]))


def NaturalMinorScale(Chordlist):

    print(ChordList)
    print("II-V-I: %s %s %s" % (ChordList[1], ChordList[4], ChordList[0]))


def HarmonicMinorScale(Chordlist):

    print(ChordList)
    print("II-V-I: %s %s %s" % (ChordList[1], ChordList[4], ChordList[0]))


def MelodicMinorScale(ChordList):

    print(ChordList)
    print("II-V-I: %s %s %s" % (ChordList[1], ChordList[4], ChordList[0]))


def main():

    print("=============================================")
    print("=     HARMONIC ANALYSIS TIP SHEET           =")
    print("=============================================\n")

    parser = argparse.ArgumentParser(description='Lorem Ipsum')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose flag')
    parser.add_argument('--key', '-k', required=True, help='key to analyse')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()

    key = args.key

    index = check_key(key)
    if (index < 0):
        print("%s is not a regular key" % key)
        exit()


    sign = getSignOfKey(key)
    
    Scale(index, sign, "Major")
    Scale(index, sign, "NaturalMinor")
    Scale(index, sign, "HarmonicMinor")
    Scale(index, sign, "MelodicMinor")



if __name__ == '__main__':

    main()

