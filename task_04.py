#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple alarm"""

DAY = raw_input("What day is it? ").lower()[:3]
TIME = int(raw_input("Please enter the time as a four"
                     " digit number without a colon: "))
SNOOZE = True if DAY == "sat" or DAY == "sun" or TIME < 600 else False
if not SNOOZE:
    print "BEEP!" * 5
