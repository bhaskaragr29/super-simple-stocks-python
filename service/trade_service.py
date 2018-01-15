def get_trade_by_stock_id(trades, stock_id):
    return [trade for trade in trades if trade.stock_id == stock_id]

def get_trade_by_stock_id_time_difference(trades = [], stock_id = 0, seconds = 60):
    import time
    current_time = time.time()
    
    return [trade for trade in trades if trade.stock_id == stock_id and trade.timestamp - current_time <= seconds* 1000] 