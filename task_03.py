#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nested statements"""

CHOICE_1 = raw_input("Please choose between Seattle Gray"
                     " or Manatee ")
CHOICE_2 = ""
CHOICE_3 = ""
if CHOICE_1 == "Seattle Gray" or CHOICE_1 == "Manatee":
    BASE = CHOICE_1
    if BASE == "Seattle Gray":
        CHOICE_2 = raw_input("Please choose between"
                             " Ceramic Glaze or Cumulus Nimbus")
        if CHOICE_2 == "Ceramic Glaze" or "Cumulus Nimbus":
            ACCENT = CHOICE_2
            if ACCENT == "Ceramic Glaze":
                HIGHLIGHT = raw_input("Please choose between"
                                      " Basically White or White")
            elif ACCENT == "Cumulus Nimbus":
                HIGHLIGHT = raw_input("Please choose between"
                                      " Off-White or Paper White")
    elif BASE == "Manatee":
        CHOICE_2 = raw_input("Please choose between Platinum Mist"
                             " or Spartan Sage")
        if CHOICE_2 == "Platinum Mist" or "Spartan Sage":
            ACCENT = CHOICE_2
            if ACCENT == "Platinum Mist":
                HIGHLIGHT = raw_input("Please choose between"
                                      " Bone White or Just White")
            elif ACCENT == "Spartan Sage":
                HIGHLIGHT = raw_input("Please choose between"
                                      " Fractal White or Not White")


print "The colors are {c1}, {c2}, {c3}.".format(c1=BASE, c2=ACCENT,
                                                c3=HIGHLIGHT)
