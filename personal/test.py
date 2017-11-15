#!/usr/bin/env python

import threading
import datetime

def printit():
    threading.Timer(5.0, printit).start()
    print(datetime.datetime.now())
    #for x in range(1000):
    #    y = x*x*x
printit()
