#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compound interest calculator"""

from decimal import Decimal
NAME = raw_input("What is your name? ")
PRINCIPAL = int(raw_input("What is the amount being borrowed? "))
YEARS = int(raw_input("How many years is this loan being borrowed? "))
QUALIFY = raw_input("Are you qualified for this loan?"
                    " Acceptable answers are either: Yes, y, No, or n")
TOTAL = True
if PRINCIPAL <= 200000 and PRINCIPAL >=0:
    if YEARS <= 15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0363")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0465")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0404")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0498")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS >=21 and YEARS <=21:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0577")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0639")
        else:
            TOTAL = None
            RATE = 0
    else:
        TOTAL = None
        RATE = 0
elif PRINCIPAL >= 200000 and PRINCIPAL <=999999:
    if YEARS <= 15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0302")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0398")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0327")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0408")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS >= 21 and YEARS <=30:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0466")
        else:
            TOTAL = None
            RATE = 0
    else:
        TOTAL = None
        RATE = 0
elif PRINCIPAL > 1000000:
    if YEARS <=15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0205")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0262")
        else:
            TOTAL = None
            RATE = 0
    else:
        TOTAL = None
        RATE = 0
else:
    TOTAL = None
    RATE = 0

if TOTAL:
    TOTAL = int(round(PRINCIPAL*(1 + RATE/12)**(12*YEARS)))

REPORT = """
Loan Report for: {name}
------------------------------------------------------------------------------
     Principal:      ${prin:>15,}
     Duration:       {dur:>15}
     Pre-qualified?: {qual:>15}
     
     Total:          ${tot:>15,}"""
if TOTAL:
    REPORT = REPORT.format(name=NAME, prin=PRINCIPAL,
                           dur=str(YEARS)+"yrs",
                           qual=QUALIFY, tot=TOTAL)
    print REPORT
else:
    REPORT = REPORT.format(name= NAME, prin=PRINCIPAL,
                           dur=str(YEARS)+"yrs",
                           qual=QUALIFY, tot="None")
    print REPORT
