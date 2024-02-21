#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: xplore
# GNU Radio version: 3.10.8.0

import sys
import math
import matplotlib.pyplot as plt


## IQ信号相加法



# -cosx + sinx = -√2cos(x+π/4)
# cosx-sinx = √2cos(x+π/4)
# cosx+sinx = √2sin(x+π/4)
# -cosx-sinx = -√2sin(x+π/4)



import sys
import math
import matplotlib.pyplot as plt

def array_add(arry1, arry2):
     return [arry1[j] + arry2[j] for j in range(len(arry1))]


def main(argv):
    info = "hello"

    FREQ = 1500000
    MAX_BPS = 125000000
    code = 0xAA
    N = MAX_BPS / FREQ
    ADC_BIT = 8
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
    I = []
    Q = []
    I_CS = []
    Q_CS = []
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
                I = I + sinx
                Q = Q + cosx
                I_CS.append(0)
                Q_CS.append(0)
            elif d == 0x01:
                I = I + sinx
                Q = Q + ncosx
                I_CS.append(0)
                Q_CS.append(-1)
            elif d == 0x02:
                I = I + nsinx
                Q = Q + cosx
                I_CS.append(-1)
                Q_CS.append(0)
            else:
                I = I + nsinx
                Q = Q + ncosx
                I_CS.append(-1)
                Q_CS.append(-1)
            scode = scode >> 2
            bits = bits + 2
        byte = byte + 1
    seq = array_add(I, Q)
    X1 = range(0,len(I))
    X2 = range(0,len(Q))
    X3 = range(0,len(seq))
    print("X1 = %d X2 = %d X3 = %d" % (len(X1), len(X2), len(X3)))
    plt.subplot(221)
    plt.plot(X1,I)
    plt.subplot(222)
    plt.plot(X2,Q)
    plt.subplot(223)
    plt.plot(X3,seq)
    plt.subplot(224)
    plt.scatter(I_CS,Q_CS)
    plt.show()
   



if __name__ == '__main__':
  main(sys.argv)
