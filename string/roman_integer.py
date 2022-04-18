class Solution:
    def romanToInt(self, s:str):
        default = {
            'IV': 4,
            'IX': 9,
            'XL':40,
            'XC':90,
            'CD':400, 
            'CM':900
        }
        roman_char = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }
        
        if s in default:
            return default[s]
        
        # if s is not in the special roman character
        sum_int=0
        for key in default.keys():
            count_sub_str = s.count(key)
            sum_int = sum_int + (count_sub_str*default[key])
            s = s.replace(key,'')
        for char in s:
            if char in roman_char:
                sum_int = sum_int +roman_char[char]
        return sum_int
if __name__ == '__main__':
    
    sol = Solution()
    roman_letter = 'LVIII'
    print(sol.romanToInt(roman_letter))