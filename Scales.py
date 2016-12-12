#!/usr/bin/env python3
# vim: number tabstop=4 expandtab shiftwidth=4 softtabstop=4 autoindent textwidth=100
# fileformat=unix 

"""

*** Description ***

    Scales.py ist ein Modul, dass verschiedene Skalen als
    Analyse-Unterstuetzung aufbereitet.

    Copyright (C) 2016  Dieter Engemann <dieter@engemann.me>

"""
import config

def MajorScale(chordList):


    print("%s minor is the relative minor of %s major." % (chordList[5],
    chordList[0]))

    print("II       V        I")
    print("%-9s%-9s%-9s\n" % (  chordList[1], 
                                chordList[4], 
                                chordList[0]))

    triSub = chordList[1][0] + "b7"
    print("V        bII   Tritonus-Substituion")
    print("%-9s%-9s\n" % (chordList[4], triSub))

    print("Akkord   Zwischendominante         Doppeldominante")

    for i in range(1,6):
        ch = chordList[i][0]
        print("%-8s" % chordList[i], end="") 
        n = config.CircleOfFifth.index(ch)
        print("%-8s %d" % (ch, n))

