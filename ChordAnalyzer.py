#!/usr/bin/env python3
# vim: number tabstop=4 expandtab shiftwidth=4 softtabstop=4 autoindent textwidth=100
# fileformat=unix 

"""

*** Description ***

    ChordAnalzyer.py is a ool to show the basic chords and scales
    to analyse jazz pieces

    Copyright (C) 2016  Dieter Engemann <dieter@engemann.me>

"""

import argparse

ChordList = ("C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B" )
CircleOfFifth = ("C", "G", "D", "A", "E", "B", "F#", "C#", "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F")

MajorList = (("maj7",0), ("m7",2), ("m7",4) , ("maj7",5), ("7",7), ("m7",9), ("m7b5",11))
NaturalMinorList = (("m7",0), ("m7b5",2), ("maj7",3) , ("m7",5), ("m7",7), ("maj7",8), ("7",10))
HarmonicMinorList = (("m(maj7)",0), ("m7b5",2), ("maj7#5",3) , ("m7",5), ("7(b9)",7), ("maj7",8), ("dim7",11))
MelodicMinorList = (("m(maj7)",0), ("m7",2), ("maj7#5",3) , ("7",5), ("7",7), ("m7b5",9), ("m7b5",11))


def Scale(ChordIndex, sign, ScaleType):
    """ print the scale beginning from the root note form a scale

        
        Different type of scales can be used. 
        :param ChordIndex:     "root note" index of the scale
        :param sign:           sharp or flat scale; C-Major ist nothing
        :param ScaleType:      Type of scale: Major, HarmonicMinor etc.
    """

    clist = []
    nlist = []

    if (ScaleType == "Major"):
        ScaleList = MajorList
    if (ScaleType == "NaturalMinor"):
        ChordIndex = ChordIndex + 9
        ScaleList = NaturalMinorList
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
        print("%-9s" % c, end="")

    print("\n\n")

    if (ScaleType == "Major"):
        MajorScale(clist)
    if (ScaleType == "NaturalMinor"):
        HarmonicMinorScale(clist)
    if (ScaleType == "HarmonicMinor"):
        HarmonicMinorScale(clist)
    if (ScaleType == "MelodicMinor"):
        MelodicMinorScale(clist)

    print("\n\n")


def check_key(key):
    """
        Ueberprueft, ob der uebergebene "key" eine gueltige Tonart ist.

        Gibt den Index fuer die Tonart-Liste zurueck (C=0, C#/Db=1, ...)
        :param key: 
        :return: index of key
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


def MajorScale(chordList):

    print("%s minor is the relative minor of %s major." % (chordList[5],
    chordList[0]))

    print("II       V        I")
    print("%-9s%-9s%-9s\n" % (chordList[1], chordList[4], chordList[0]))

    triSub = chordList[1][0] + "b7"
    print("V        bII   Tritonus-Substituion")
    print("%-9s%-9s\n" % (chordList[4], triSub))

def NaturalMinorScale(chordlist):

    print("II       V        I")
    print("%s %s %s" % (chordList[1], chordList[4], chordList[0]))


def HarmonicMinorScale(chordList):

    print("II       V        I")
    print("%s %s %s" % (chordList[1], chordList[4], chordList[0]))


def MelodicMinorScale(chordList):

    print("II-V-I: %s %s %s" % (chordList[1], chordList[4], chordList[0]))


def main():

    parser = argparse.ArgumentParser(description='Lorem Ipsum')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose flag')
    parser.add_argument('--key', '-k', required=True, help='key to analyse')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    print("=============================================")
    print("=     HARMONIC ANALYSIS TIP SHEET           =")
    print("=============================================\n")

    args = parser.parse_args()

    index = check_key(args.key)
    if (index < 0):
        print("%s is not a regular key" % args.key)
        exit()


    sign = getSignOfKey(args.key)
    
    Scale(index, sign, "Major")
    Scale(index, sign, "NaturalMinor")
    Scale(index, sign, "HarmonicMinor")
    Scale(index, sign, "MelodicMinor")



if __name__ == '__main__':

    main()

