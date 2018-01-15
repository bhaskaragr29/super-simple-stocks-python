#! /usr/bin/env python

import itertools
import functools
import time

from model import Stock, Trade
from service import StockService
from decimal import *

stock_count = itertools.count(1)
trade_count = itertools.count(1)

stock_list = [
    Stock("TEA", "COMMON", 23, 0, 100, stock_count.next()), 
    Stock("POP", "COMMON", 8, 0, 100, stock_count.next()),
    Stock("ALE", "COMMON", 12, 0, 109, stock_count.next()),
    Stock("GIN", "PREFFERED", 23, 2, 100, stock_count.next()),
    Stock("JOE", "COMMON", 13, 0, 250, stock_count.next())
]
symbol_list = [stock.symbol for stock in stock_list]
service = StockService({stock.symbol:stock for stock in stock_list})


def read_stock_symbol():
    """ Reading Stock Symbol from input"""
    symbol = ""
    while(True):
        symbol = raw_input("Enter stock symbol:")
        if(symbol in symbol_list):
            break
        else:
            print("Wrong symbol enter again")
    return symbol

def read_trade_quantity():
    """ Get Trade Quantity from input"""
    q = 0
    while(True):
        q = raw_input("Enter trade quantity:")
        
        if q.decode('utf-8').isnumeric():
            break
        else:
            print("Wrong quantity")
    return q

def read_trade_price():
    """ Get Trade Price from input """
    trade_price = float(0)
    while(True):
        q = raw_input("Enter trade price:")
        try:
            trade_price = float(q)
            break
        except:
            print("Invalid trade price.  Try again.")
    return trade_price

if __name__ == '__main__':
    print('Please select stocks from '+(",".join(symbol_list)))
    trades = []
    while(True):
        symbol = read_stock_symbol()
        market_price = read_trade_price()
        q = read_trade_quantity()
        
        current_stock = service.get_stock_by_symbol(symbol)
        
        trades.append(Trade(trade_count.next(), time.time(), current_stock.id, q, market_price, "BUY"))

        print("PE Ratio for "+symbol+":"+str(round(service.get_pe_ratio(market_price, symbol),3 )))
        print("Dividend yield for "+symbol+":"+str(round(service.get_dividend_yeild(market_price, symbol), 3)))
        print("VSMP for "+symbol+":"+str(round(service.get_volume_weighted_stock_price(trades, current_stock.id),3)))
        print("Geometric Mean for "+symbol+":"+str(round(service.get_geometric_mean(trades, current_stock.id), 3)))
        print("\n")