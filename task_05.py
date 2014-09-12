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
if PRINCIPAL < 200000 and PRINCIPAL >= 0:
    if YEARS < 16:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0363")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0465")
    elif YEARS < 21:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0404")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0498")
    elif YEARS <= 30:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0577")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0639")
    else:
        TOTAL = None
        RATE = 0
elif PRINCIPAL < 1000000 and PRINCIPAL >= 200000:
    if YEARS < 16:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0302")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0398")
    elif YEARS < 21:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0327")
        elif QUALIFY == "No" or QUALIFY == "n":
            RATE = Decimal("0.0408")
    elif YEARS <= 30:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0466")
        else:
            TOTAL = None
            RATE = 0
    else:
        TOTAL = None
        RATE = 0
elif PRINCIPAL >= 1000000:
    if YEARS < 16:
        if QUALIFY == "Yes" or QUALIFY == "y":
            RATE = Decimal("0.0205")
        else:
            TOTAL = None
            RATE = 0
    elif YEARS < 21:
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


if TOTAL:
    TOTAL = int(round(PRINCIPAL * (1 + RATE/12)**(12 * YEARS)))

REPORT = """
Loan Report for: {0}
------------------------------------------------------------------------------
     Principal:      {1:>15}
     Duration:       {2:>15}
     Pre-qualified?: {3:>15}
     
     Total:          {4:>15}"""
if TOTAL:
    REPORT = REPORT.format(NAME,
                           ("$" + str('{:,}'.format(PRINCIPAL))),
                           str(YEARS)+"yrs",
                           QUALIFY, ("$"+str('{:,}'.format(TOTAL))))
    print REPORT
else:
    REPORT = REPORT.format(NAME,
                           ("$" + str('{:,}'.format(PRINCIPAL))),
                           str(YEARS)+"yrs",
                           QUALIFY, str(TOTAL))
    print REPORT
