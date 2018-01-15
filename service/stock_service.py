from formula import *
from trade_service import *

class StockService:
    """ Stock Service Class """
    def __init__(self, beverages_stocks):
        self.beverages_stocks = beverages_stocks
    
    def get_stock_by_symbol(self, symbol):
        """ Get Stock by Symbol """
        return self.beverages_stocks.get(symbol)
    
    def get_pe_ratio(self, market_price = 0.0, symbol = ""):
        """ Get PE ratio service function """
        stock = self.beverages_stocks.get(symbol)
        return get_raw_pe_ratio(market_price, stock.last_dividend)

    def get_dividend_yeild(self, market_price = 0.0, symbol = ""):
        """ Get Dividend Yeild service function """
        stock = self.beverages_stocks.get(symbol)

        return 0 if market_price < 0 or stock is None else get_raw_dividend_yield( 
            last_dividend = stock.last_dividend, 
            market_price = market_price, 
            fixed_dividend = stock.fixed_dividend, 
            par_value = stock.par_value,
            stock_type = stock.stock_type
        )
    
    def get_geometric_mean(self, trades = [], stock_id = 0):
        """ Get Geometric Mean service function """
        filtered_list = get_trade_by_stock_id(trades, stock_id)
        return get_raw_geometric_mean([trade.trade_price for trade in filtered_list]) 

    def get_volume_weighted_stock_price(self, trades = [], stock_id = 0, seconds = 60):
        """ Get Volume Weighted Stock Price service function """
        filtered_list = get_trade_by_stock_id_time_difference(trades, stock_id, seconds)
        return get_raw_volume_weighted_stock_price([(trade.trade_price, trade.quantity) for trade in filtered_list])