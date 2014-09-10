#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nested statements"""

CHOICE_1 = raw_input("Please choose between Seattle Gray"
                     " or Manatee ")
CHOICE_2 = raw_input("Please choose between Ceramic Glaze"
                     " or Cumulus Nimbus ")
CHOICE_7 = raw_input("Please choose between Basically White"
                     " or Off-White ")
if CHOICE_1 == "Seattle Gray" or CHOICE_1 == "Manatee":
    BASE = CHOICE_1
    if CHOICE_2 == "Ceramic Glaze" or CHOICE_2 == "Cumulus Nimbus":
        ACCENT = CHOICE_2
    if CHOICE_7 == "Basically White" or CHOICE_7 == "Off-White":
            HIGHLIGHT = CHOICE_7

print "The colors chosen are {a}, {b}, {c}.".format(a=BASE, b=ACCENT,
                                                    c=HIGHLIGHT)
