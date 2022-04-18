class Solution:

    def maxProfit(self, prices):
        profit=[]
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[i]<prices[j]:
                    profit.append(prices[j]-prices[i])
        if len(profit)==0:
            return 0
        return max(profit)

                

if __name__ == '__main__':
    arr= [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(arr))