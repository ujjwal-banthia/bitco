#!/usr/bin/env python

import talib
import numpy
import threading
import argparse
import datetime

#Argument Parser Code start
#parser = argparse.ArgumentParser(description="get following data for given ticker")
#parser.add_argument("-s","--symbol", help="Ticker", default="btcusd")
#parser.add_argument("-f","--freq",help="Frequency in miliseconds", type=int, default=10000)
#
#arguments = parser.parse_args()
#args = vars(arguments)
##Argument Parser Code end
#
#
#def mainB(args):
#    freq = float(args["freq"])
#    symbol = args["symbol"]
#    ema(freq, symbol, client)
#
#def ema(freq, symbol, client):
#    try:
#        threading.Timer(freq/1000,ema,[freq,symbol,client]).start()
#    except (KeyboardInterrupt, SystemExit):
#        cleanup_stop_thread()
#        sys.exit() 
#


close = numpy.random.random(100)
real = talib.EMA(close, timeperiod=10)
print real
