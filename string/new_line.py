class Solution:
    def new_line(self, s, pos):
        space_counter=0
        for idx,ch in enumerate(s):
            if ch==' ':
                space_counter=idx
            
            if ch==' ' and (idx+1)%pos==0:
                s = s[:idx]+'\n'+s[idx+1:]
            
            elif ch!=' ' and (idx+1)%pos==0:
                s = s[:space_counter]+'\n'+s[space_counter+1:]
        return s
        
if __name__ == '__main__':
    sol = Solution()
    
    s = "I am the Sword in the Darkness I am the watcher on the walls. I'm the fire that burns against the cold. ~Night's Watch"
    pos=12
    print(sol.new_line(s,pos))