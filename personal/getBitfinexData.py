#!/usr/bin/env python3


import bitfinex
from bitfinex.client import Client
import argparse
import filelock
import threading
import datetime

#Argument Parser Code start
parser = argparse.ArgumentParser(description="get following data for given ticker")
parser.add_argument("-s","--symbol", help="Ticker", default="btcusd")
parser.add_argument("-f","--freq",help="Frequency in miliseconds", type=int, default=10000)

arguments = parser.parse_args()
args = vars(arguments)
#Argument Parser Code end

def mainB(args):
    freq = float(args["freq"])
    symbol = args["symbol"]
    client = Client()
    while True:
        loopTickerB(freq, symbol, client)

def loopTickerB(freq, symbol, client):
#    try:
#        threading.Timer(freq/1000,loopTickerB,[freq,symbol,client]).start()
#    except (KeyboardInterrupt, SystemExit):
#        cleanup_stop_thread()
#        sys.exit() 
    currentValues = {**client.ticker(symbol), **client.today(symbol)}
    last = currentValues['last_price']
    quoteVolume = currentValues['volume']
    high24hr = currentValues['high']
    highestBid = currentValues['bid']
    low24hr = currentValues['low']
    lowestAsk = currentValues['ask']
    dataDate = currentValues['timestamp']
    dataDate = datetime.datetime.utcfromtimestamp(dataDate)

    with open("/home/ubanthia/bitco/personal/data.txt", "a") as myFile:
        myFile.write(str(dataDate)+" Period: "+str(freq)+"ms Symbol: "+str(symbol)+" LastTrade: "+str(last)+" Bid: "+str(highestBid)+" Ask: "+str(lowestAsk)+" QuoteVolume: "+str(quoteVolume)+" 24hrLow: "+str(low24hr)+" 24hrHigh: "+str(high24hr)+"\n\n")
    
    print("%s Period: %sms Symbol: %s LastTrade: %s Bid: %s Ask: %s QuoteVolume: %s 24hrLow: %s 24hrHigh: %s " % (dataDate, freq, symbol, last, highestBid, lowestAsk, quoteVolume, low24hr, high24hr))

mainB(args)

