class Solution:
    def mySqrt(self, x: int):
        r=x
        while r*r>x:
            r= (r+x/r)//2
        return int(x)