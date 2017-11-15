#!/usr/bin/env python3

from btfxwss import BtfxWss
import logging
import sys
import time
import os
import filelock
import argparse
import threading
import datetime

#Argument Parser Code start
parser = argparse.ArgumentParser(description="get following data for given ticker")
parser.add_argument("-s","--symbol",help="Ticker")
parser.add_argument("-f","--freq",help="Frequency in miliseconds", type=int)
arguments = parser.parse_args()

args = vars(arguments)

if args["symbol"] is not None:
    symbol = args["symbol"]
else:
    symbol = "BTCUSD"

if args["freq"] is not None:
    freq = args["freq"]
else:
    freq = 5000
#Argument Parser Code end

#path = os.path.abspath(BtfxWss.__file__)
#print(python --version)

log = logging.getLogger(__name__)

fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)

log.addHandler(sh)
log.addHandler(fh)
logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])

wss = BtfxWss()
wss.start()

# Wait (indefinitely) for the websocket connection to happen.
wss.conn.connected.wait()


# Subscribe to some channels
#wss.subscribe_to_ticker(symbol)
#wss.subscribe_to_order_book(symbol)

# Do something else
t = time.time()
while time.time() - t < 10:
    pass

# Accessing data stored in BtfxWss:
def tickerLoop(wss,symbol,freq):
    #threading.Timer(freq/1000,tickerLoop,[wss,symbol,freq]).start()
    wss.subscribe_to_ticker(symbol)
    ticker_q = wss.tickers(symbol)  # returns a Queue object for the pair.
    while not ticker_q.empty():
        tempTuple = ticker_q.get()
        data = tempTuple[0][0]
        dataTime = tempTuple[1]
        bid = data[0]
        bidSize = data[1]
        ask = data[2]
        askSize = data[3]
        dailyChange = data[4]
        dailyChangePer = data[5]
        lastPrice = data[6]
        volume = data[7]
        high = data[8]
        low = data[9]
        lock = filelock.FileLock("/home/ubanthia/bitco/personal/data.txt")
        lock.acquire()
        with open("/home/ubanthia/bitco/personal/data.txt", "a") as myFile:
            myFile.write(str(dataTime)+" Exchange: Bitfinex Period: "+str(freq)+"ms Symbol: "+str(symbol)+" LastTrade: "+str(lastPrice)+" DailyChangePercent: "+str(dailyChangePer)+" Bid: "+str(bid)+" BidSize: "+str(bidSize)+" Ask: "+str(ask)+" AskSize: "+str(askSize)+" Volume: "+str(volume)+" 24hrLow: "+str(low)+" 24hrHigh: "+str(high)+"\n\n")
        lock.release()
        print(data)

while True:
    tickerLoop(wss, symbol, freq)
    time.sleep(5)

# Unsubscribing from channels:
#wss.unsubscribe_from_ticker(symbol)
#wss.unsubscribe_from_order_book(symbol)

# Shutting down the client:
#wss.stop()
