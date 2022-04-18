class Solution:
    
    def maxProfit(self, prices):
        l,r= 0,1
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[l]<prices[r]:
                profit=  prices[r]-prices[l]
                max_profit = max(max_profit,profit)
            
            else:
                # this gets the minimum value of the list
                l=r
            r+=1
        return max_profit            
                
if __name__ == '__main__':
    arr= [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(arr))