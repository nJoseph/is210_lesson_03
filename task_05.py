#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compound interest calculator"""

from decimal import Decimal
NAME = raw_input("What is your name? ")
PRINCIPAL = int(raw_input("What is the amount being borrowed? "))
YEARS = int(raw_input("How many years is this loan being borrowed? "))
QUALIFY = raw_input("Are you qualified for this loan?"
                    " Acceptable answers are either: Yes, y, No, or n")
TOTAL = ""
if PRINCIPAL < 200000:
    if YEARS <= 15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0363")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0465")
        else:
            TOTAL = None
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0404")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0498")
        else:
            TOTAL = None
    elif YEARS >=21 and YEARS <=21:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0577")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0639")
        else:
            TOTAL = None
    else:
        TOTAL = None
elif PRINCIPAL >= 200000 and PRINCIPAL <=999999:
    if YEARS <= 15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0302")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0398")
        else:
            TOTAL = None
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0327")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0408")
        else:
            TOTAL = None
    elif YEARS >= 21 and YEARS <=30:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0466")
        else:
            TOTAL = None
    else:
        TOTAL = None
elif PRINCIPAL >= 1000000:
    if YEARS <=15:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0205")
        else:
            TOTAL = None
    elif YEARS >= 16 and YEARS <=20:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0262")
        else:
            TOTAL = None
    else:
        TOTAL = None
else:
    TOTAL = None

if TOTAL != None:
    TOTAL = int(round(PRINCIPAL*(1 + RATE/12)**(12*YEARS)))
else:
    print "ERROR. You did not complete some or more of the fields."

EVALUATION = """
Loan Report for: {name}
------------------------------------------------------------------------------
     Principal:      {prin:>15}
     Duration:       {dur:>15}
     Pre-qualified?: {qual:>15}
     Total:          {tot:>15}"""
REPORT = EVALUATION.format(name=NAME, prin="$"+str(PRINCIPAL)
                           , dur=str(YEARS)+"yrs",
                           qual=QUALIFY, tot="$"+str(TOTAL))
print REPORT

