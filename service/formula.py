from decimal import Decimal

def get_raw_pe_ratio(market_price, dividend):
    """ Get PE Ratio and return data in Decimal format"""
    return 0 if (dividend <= 0 or market_price <= 0) else Decimal(market_price) / Decimal(dividend)

def get_raw_dividend_yield(**kwargs):
    """ get Dividend Yeild and get data in Decimal Format"""

    dividend_yield_value = Decimal(0) 
    if kwargs:
        last_dividend = kwargs.get('last_dividend')
        market_price = kwargs.get('market_price')
        fixed_dividend = kwargs.get('fixed_dividend')
        par_value = kwargs.get('par_value')
        stock_type = kwargs.get('stock_type')
       

        if market_price > 0:
            if stock_type is 'COMMON':
                dividend_yield_value =  Decimal(last_dividend)/Decimal(market_price)
            else:
                dividend_yield_value = Decimal(par_value)*(Decimal(fixed_dividend/100.0)) / Decimal(market_price)
    return  dividend_yield_value
      
def get_raw_geometric_mean(market_prices):
    """ get Geometric Mean for market prices"""
    market_mean = reduce(lambda x,y: x*y, market_prices)
    return Decimal(pow(market_mean, 1.0/len(market_prices)))

def get_raw_volume_weighted_stock_price(trades):
    """ Get VSMP for Stock """
    quantity = sum_trade_quantity = 0.0
    
    for mp, qty in trades:
        sum_trade_quantity +=  (mp * qty)
        quantity +=  qty
    
    return Decimal(0) if quantity == 0 or sum_trade_quantity== 0 else Decimal(sum_trade_quantity/quantity)