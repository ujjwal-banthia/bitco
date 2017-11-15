#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:30:50 2017

@author: ubanthia
"""

from poloniex import poloniex
import time
import sys
import datetime
import logging

# =============================================================================
# def setup_custom_logger(name):
#     formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
#                                   datefmt='%Y-%m-%d %H:%M:%S')
#     handler = logging.FileHandler('log.txt', mode='w')
#     handler.setFormatter(formatter)
#     screen_handler = logging.StreamHandler(stream=sys.stdout)
#     screen_handler.setFormatter(formatter)
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)
#     logger.addHandler(handler)
#     logger.addHandler(screen_handler)
#     return logger
# 
# =============================================================================

def main(argv):
#    logger = setup_custom_logger('tradebot')
    period = 1
    conn = poloniex('J6S7XE6H-W1RF1FPY-WESQ7BQI-YHMBXF57','e0c2deabb2d1e281d8cb5dfc0c8bd3b23366a91c2bef559081967b27795c28a9d3d8442037f33764fce91fc293d009cbfb56097ac9b21db769908587ddc61d6a')
    
    while True:
        #print logger.info('')
        currentTicker = conn.api_query("returnTicker")
        print(datetime.datetime.now() + ' ' + currentTicker['USDT_BTC'])
        time.sleep(int(period))
        
        
if __name__  == "__main__":
    main(sys.argv[1:])
