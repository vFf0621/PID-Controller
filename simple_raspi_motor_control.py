# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import RPi.GPIO as IO
IO.setmode(IO.BCM)
IO.setup(17, IO.IN)
IO.setup(27, IO.IN)

curr= 0, 0
t0 = time.time()
while True:
    prev = curr
    curr = IO.input(17), IO.input(27)
    if curr[0] != prev[0] or curr[1] != prev[1]:
        t1 = time.time()    
        print(t1 - t0)
        t0 = t1