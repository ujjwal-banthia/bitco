#!/usr/bin/env python

import time
import sys, getopt
import datetime
from poloniex import poloniex
import argparse
import threading

#Argument Parser Code start
parser = argparse.ArgumentParser(description="get following data for given ticker")
parser.add_argument("-s", "--symbol", help="Ticker", default="USDT_BTC")
parser.add_argument("-f", "--freq", help="Frequency in miliseconds", type=int, default=10000)

arguments = parser.parse_args()
args = vars(arguments)
#Argument Parser Code end

def getData(arg):
    freq = float(args["freq"])
    symbol = args["symbol"]
    conn = poloniex('key goes here','key goes here')
    loopTicker(freq, symbol, conn)
    

def loopTicker(freq, symbol, conn):
    try:
        threading.Timer(freq/1000,loopTicker,[freq,symbol,conn]).start()
    except (KeyboardInterrupt, SystemExit):
        cleanup_stop_thread()
        sys.exit() 
    currentValues = conn.api_query("returnTicker")
    currentValues = currentValues[symbol]
    dataDate = datetime.datetime.now()
    
    last = currentValues['last']
    quoteVolume = currentValues['quoteVolume']
    high24hr = currentValues['high24hr']
    isFrozen = currentValues['isFrozen']
    highestBid = currentValues['highestBid']
    percentChange = currentValues['percentChange']
    low24hr = currentValues['low24hr']
    lowestAsk = currentValues['lowestAsk']
    securityId = currentValues['id']
    baseVolume = currentValues['baseVolume']
    
    print "%s Period: %sms Symbol: %s Id: %s LastTrade: %s ChangePercent: %s Bid: %s Ask: %s QuoteVolume: %s NetVolume: %s 24hrLow: %s 24hrHigh: %s Frozen: %s" % (dataDate, freq, symbol, securityId, last, percentChange, highestBid, lowestAsk, quoteVolume, baseVolume, low24hr, high24hr, isFrozen)
    
    with open("/home/ubanthia/bitco/personal/data.txt", "a") as myFile:
        myFile.write(str(dataDate)+" Period: "+str(freq)+"ms Symbol: "+str(symbol)+" Id: "+str(securityId)+" LastTrade: "+str(last)+" ChangePercent: "+str(percentChange)+" Bid: "+str(highestBid)+" Ask: "+str(lowestAsk)+" QuoteVolume: "+str(quoteVolume)+" NetVolume: "+str(baseVolume)+" 24hrLow: "+str(low24hr)+" 24hrHigh: "+str(high24hr)+" Frozen: "+str(isFrozen)+"\n\n")

getData(args)

