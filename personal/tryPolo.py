#!/usr/bin/env python

from poloniex import poloniex

polo=poloniex('J6S7XE6H-W1RF1FPY-WESQ7BQI-YHMBXF57','e0c2deabb2d1e281d8cb5dfc0c8bd3b23366a91c2bef559081967b27795c28a9d3d8442037f33764fce91fc293d009cbfb56097ac9b21db769908587ddc61d6a')
While True:
    data = polo.returnTicker()
    print data
