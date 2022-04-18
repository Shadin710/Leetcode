class Solution:
    def maxProfit(self, prices):
        prev_pointer = 0
        curr_pointer = 1
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[prev_pointer]<prices[curr_pointer]:
                profit = prices[curr_pointer]-prices[prev_pointer]
                max_profit = max(max_profit,profit)
            else:
                prev_pointer=curr_pointer
            curr_pointer+=1
        
        return max_profit
if __name__ == '__main__':
    
    sol = Solution()
    arr= [7,1,5,3,6,4]
    print(sol.maxProfit(arr))   