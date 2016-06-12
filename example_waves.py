#!/usr/bin/env python
import numpy as np
import sys

dim = 32

def wave(period=20.0, phase=0.0, angle=np.pi/4, ampl=127, mean = 127):
    ph = np.arange(dim, dtype=np.float16)*2*np.pi/period
    xph = np.cos(angle)*ph
    yph = np.sin(angle)*ph
    phm = np.tile(xph,(dim,1)) + np.tile(yph,(dim,1)).transpose()
    return np.uint8(np.clip(np.sin(phm + phase) * ampl + mean,0,255))

def stream(r, g, b):
    sys.stdout.write('\x01')
    rs = r.flatten()
    gs = g.flatten()
    bs = b.flatten()
    sys.stdout.write(np.stack([rs,gs,bs], axis=1).flatten().tobytes())

i = 0.0
while True:
    i += 0.01
    r = wave(angle = i / 5, period = np.sin(i/30) * 40 )
    g = wave(phase = 2 * i)
    b = wave(phase = 3 * i)
    stream(r,g,b)
