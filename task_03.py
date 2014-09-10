#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nested statements"""

BASE = "You didn't specify."
ACCENT = "You didn't specify."
HIGHLIGHT = "You didn't specify."
CHOICE_1 = ""
CHOICE_2 = ""
CHOICE_3 = ""
CHOICE_4 = ""
CHOICE_5 = ""
CHOICE_6 = ""
CHOICE_7 = ""
CHOICE_1 = raw_input("Please choose between Seattle Gray"
                     " or Manatee ")
CHOICE_2 = raw_input("Please choose between Ceramic Glaze"
                     " or Cumulus Nimbus ")
CHOICE_3 = raw_input("Please choose between Platinum Mist"
                     " or Spartan Sage ")
CHOICE_4 = raw_input("Please choose between Basically White"
                     " or White ")
CHOICE_5 = raw_input("Please choose between Off-White"
                     " or Paper White ")
CHOICE_6 = raw_input("Please choose between Bone White"
                     " or Just White ")
CHOICE_7 = raw_input("Please choose between Fractal White"
                     " or Not White ")
if CHOICE_1 == "Seattle Gray" or CHOICE_1 == "Manatee":
    BASE = CHOICE_1
    if CHOICE_2 == "Ceramic Glaze" or CHOICE_2 == "Cumulus Nimbus":
        ACCENT = CHOICE_2
    elif CHOICE_3 == "Platinum Mist" or CHOICE_3 == "Spartan Sage":
        ACCENT = CHOICE_3
    if CHOICE_4 == "Basically White" or CHOICE_4 == "White":
            HIGHLIGHT = CHOICE_4
    elif CHOICE_5 == "Off-White" or CHOICE_5 == "Paper White":
            HIGHLIGHT = CHOICE_5
    elif CHOICE_6 == "Bone White" or CHOICE_6 == "Just White":
            HIGHLIGHT = CHOICE_6
    elif CHOICE_7 == "Fractal White" or CHOICE_7 == "Not White":
            HIGHLIGHT = CHOICE_7

print "The color chosen for base is {color1}.".format(color1=BASE)
print "The color chosen for accent is {color2}.".format(color2=ACCENT)
print "The color chosen for the highlight is {color3}.".format(color3=HIGHLIGHT)
