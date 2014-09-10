#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Shows branching"""

BLOOD_NUMBER = int(raw_input("Please enter your systolic blood pressure number "))
BP_STATUS = ""
if BLOOD_NUMBER <= 89:
    BP_STATUS = "Low"
elif BLOOD_NUMBER <= 119:
    BP_STATUS = "Ideal"
elif BLOOD_NUMBER <= 139:
    BP_STATUS = "Warning"
elif BLOOD_NUMBER <= 159:
    BP_STATUS = "High"
elif BLOOD_NUMBER >= 160:
    BP_STATUS = "Emergency"

print "Your blood pressure status is {status}.".format(status=BP_STATUS)
