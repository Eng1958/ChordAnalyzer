#!/usr/bin/env python3
# vim: number tabstop=4 expandtab shiftwidth=4 softtabstop=4 autoindent textwidth=79

"""
TipSheet.py – Tool to show the basic chords and scales
to analyse jazz pieces
Copyright (C) 2016  Dieter Engemann <dieter@engemann.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import argparse

ChordList = ("C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B" )
MajorList = (("maj7",0), ("m7",2), ("m7",4) , ("maj7",5), ("7",7), ("m7",9), ("m7b5",11))
HarmonicMinorList = (("mmaj7",0), ("m7",2), ("m7",4) , ("maj7",5), ("7",7), ("m7",9), ("m7b5",11))
MelodicMinorList = (("maj7",0), ("m7",2), ("m7",4) , ("maj7",5), ("7",7), ("m7",9), ("m7b5",11))

CircleOfFifth = ("C", "G", "D", "A", "E", "B", "F#", "C#", "Cb", "Gb", "Db", "Ab", "Eb", "Bb", "F")

# ----------------------------------------------------------------------------
# Scale
# ----------------------------------------------------------------------------
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
    if (ScaleType == "HarmonicMinor"):
        ScaleList = HarmonicMinorList
    if (ScaleType == "MelodicMinor"):
        ScaleList = MelodicMinorList

    for ChordType in ScaleList:
        
        chordBase = ChordList[(ChordType[1] + ChordIndex) % len(ChordList)]
        if ("/" in chordBase):
            c = (chordBase.split("/"))
            if (sign[0] == "#"):
                chordBase = c[0]
            else:
                chordBase = c[1]
        nlist.append(chordBase)
        clist.append(chordBase + ChordType[0])

    str = "Key of %s %s (%s)" % (nlist[0], ScaleType, ' '.join(nlist))
    print(str)
    print("".ljust(len(str), '-'))

    # print("I      II     III    IV     V      VI     VII")
    str = "I      II     III    IV     V      VI     VII"
    print(str)

    for c in clist:
        print("%-7s" % c, end="")

    print("\n\n")

    if (ScaleType == "Major"):
        MajorScale()
    if (ScaleType == "HarmonicMinor"):
        HarmonicMinorScale()
    if (ScaleType == "MelodicMinor"):
        MelodicMinorScale()

    print("\n\n")

# ----------------------------------------------------------------------------
# check_key()
#
# ----------------------------------------------------------------------------
def check_key(key):
    """
        Ueberprueft, ob der uebergebene "key" eine gueltige Tonart ist.

        Gibt den Index fuer die Tonart-Liste zurueck (C=0, C#/Db=1, ...)
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

# ----------------------------------------------------------------------------
# getSignOfKey()
# ----------------------------------------------------------------------------
def getSignOfKey(key):

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
def MajorScale():

    print("IIm-V-I: %s" % ("Dm7 G7 Cmaj7"))

def HarmonicMinorScale():


    print("IIm-V-I: %s" % ("Dm7b5 G7b9 Cm7"))

def MelodicMinorScale():


    print("IIm-V-I: %s" % ("Dm7??? G7??? Cj7?????"))

# ----------------------------------------------------------------------------
# main()
# ----------------------------------------------------------------------------
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
    ## print("Key %s %s " % (key, sign))
    
    Scale(index, sign, "Major")
    Scale(index, sign, "HarmonicMinor")
    Scale(index, sign, "MelodicMinor")



if __name__ == '__main__':

    main()

