#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: xplore
# GNU Radio version: 3.10.8.0


## IQ信号相加法



# -cosx + sinx = -√2cos(x+π/4)
# cosx-sinx = √2cos(x+π/4)
# cosx+sinx = √2sin(x+π/4)
# -cosx-sinx = -√2sin(x+π/4)



import sys
import math
import numpy as np
import matplotlib.pyplot as plt



info = "hello"

FREQ = 2000000
MAX_BPS = 125000000
code = 0xAA
N = MAX_BPS / FREQ
ADC_BIT = 14
MAX_VALUE = 2**ADC_BIT
delta = 2*math.pi / N
sinx = []
cosx = []  
nsinx = []
ncosx = []

i = 0
num = 0
while i < 2*math.pi:
    value =  round(math.sin(i) * (float)( MAX_VALUE/2) + MAX_VALUE/2)
    sinx.append(value)
    i = i + delta
    num = num + 1

i = 0
num = 0
while i < 2*math.pi:
    value =  round(math.cos(i) * (float)( MAX_VALUE/2) + MAX_VALUE/2)
    cosx.append(value)
    i = i + delta
    num = num + 1


i = 0
num = 0
while i < 2*math.pi:
    value =  MAX_VALUE - round(math.sin(i) * (float)( MAX_VALUE/2) + MAX_VALUE/2)
    nsinx.append(value)
    i = i + delta
    num = num + 1

i = 0
num = 0
while i < 2*math.pi:
    value = MAX_VALUE -  round(math.cos(i) * (float)( MAX_VALUE/2) + MAX_VALUE/2)
    ncosx.append(value)
    i = i + delta
    num = num + 1

wlen = len(sinx)

seq = []
bits = 0
byte = 0
scode = code
lengt = len(info)
print(" lengt = %d" % lengt)
while byte < lengt:
    scode = ord(info[byte])
    bits = 0
    print(" scode = %x" % scode)
    while bits < 8:
        d = scode & 0x03
        print(" d = %x" % d)
        if d == 0x00:
            temp = [sinx[j] + cosx[j] for j in range(wlen)]  #sinx + cosx = √2sin(x+π/4)      
        elif d == 0x01:
            temp = [sinx[j] + ncosx[j] for j in range(wlen)]  #sinx - cosx = -√2cos(x+π/4)
        elif d == 0x02:
            temp = [nsinx[j] + cosx[j] for j in range(wlen)]  #-sinx + cosx = √2cos(x+π/4)        
        else:
            temp = [nsinx[j] + ncosx[j] for j in range(wlen)]  #-sinx - cosx = -√2sin(x+π/4)
        seq = seq + temp                
        scode = scode >> 2
        bits = bits + 2
    byte = byte + 1
 
X = range(0,len(seq))
plt.plot(X,seq)
plt.show()
