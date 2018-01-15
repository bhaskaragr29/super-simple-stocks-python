class Trade:
    """ Trade Model """
    
    def __init__(self, id, timestamp, stock_id, quantity, trade_price, indicator_type):
		self.stock_id = stock_id
		self.quantity = int(quantity)
		self.trade_price = trade_price
		self.type = indicator_type
		self.timestamp = timestamp
		self.id = id