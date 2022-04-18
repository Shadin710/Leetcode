class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        ran_len = len(ransomNote)
        mag_len = len(magazine)
        if mag_len<ran_len:
            return False
        ran_hash={}
        mag_hash={}
        for ran in ransomNote:
            if ran not in ran_hash:
                ran_hash[ran]=1
            else:
                ran_hash[ran]+=1
        for mag in magazine:
            if mag not in mag_hash:
                mag_hash[mag]=1
            else:
                mag_hash[mag]+=1
        ran_key = list(ran_hash.keys())
        
        check=0
        for key in ran_key:
            if mag_hash.get(key,-1)==-1:
                return False
            ran_char_val = ran_hash[key]
            mag_char_val= mag_hash[key]
            if mag_char_val>=ran_char_val:
                check+=1
        if check==len(ran_key):
            return True
        return False
if __name__ == '__main__':
    sol = Solution()
    ransome = 'a'
    magazine='b'
    print(sol.canConstruct(ransome,magazine))