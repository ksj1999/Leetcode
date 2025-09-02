class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = {key : val for val, key in enumerate(prices)}
        print(temp)
        maxv = max(temp)
        minv = min(temp)
-----------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = {i: p for i, p in enumerate(prices)} 

        min_price = float('inf')
        max_profit = 0

        for i in temp: 
            price = temp[i]
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

-----------------------------------------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') 
        max_profit = 0   
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
