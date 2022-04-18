class Solution:
    def longestCommonPrefix(self, strs):
        count_len = []
        for i in arr:
            count_len.append(len(i))
        min_len = min(count_len)
        min_str_index = count_len.index(min_len)
        min_str = strs[min_str_index]
        result= ''
        count_number=0
        
        for st in strs:
            max_index = []
            for i in range(min_len):
                if min_str[i]==st[i]:
                    max_index.append(i)
                    count_number+=1
                else:
                    break
        if count_number== len(strs):
            return min_str[:min(max_index)-1]
        else:
            return ""
if __name__ == '__main__':
    sol = Solution()
    
    arr = ["flower","flow","flight"]
    print(sol.longestCommonPrefix(arr))