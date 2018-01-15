class Stock:
    """ Stock Model """
    
    def __init__(self, symbol, stock_type, last_dividend, fixed_dividend, par_value, id):
        self.symbol = symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.id = id