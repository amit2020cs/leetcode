class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drinks = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            # Exchange numExchange empty bottles with one full water bottle
            exchanged_bottles = empty_bottles // numExchange
            total_drinks += exchanged_bottles
            # Update the number of empty bottles after the exchange
            empty_bottles = exchanged_bottles + empty_bottles % numExchange
            
        return total_drinks
