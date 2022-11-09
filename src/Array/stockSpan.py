class StockSpanner:

    def __init__(self):
        self.prices = []        
        self.lastRun = 0

    def next(self, price: int) -> int:
        
        self.prices.append(price)

        if (self.lastRun == 0) or price < self.prices[-2]:
            self.lastRun = 1
            return 1
        
        else: # price is greater or equal to last price

            # run is at least as long as previous run, plus itself.
            self.lastRun = self.lastRun + 1
            
            if self.lastRun == len(self.prices): #as long as the array, no need to continue
                return self.lastRun
            
            # set index to the first element that was excluded from the previous run 
            # Already know that all the prices from the previous run are lower than the current price
            i = len(self.prices) - self.lastRun - 1

            while i >= 0 and self.prices[i] <= price:
                self.lastRun += 1
                i -= 1

            return self.lastRun