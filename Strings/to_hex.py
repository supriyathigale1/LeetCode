#https://leetcode.com/problems/convert-a-number-to-hexadecimal/
class Solution:
    def toHex(self, num: int) -> str:
        #hexadecimal are to the base 16
        #0xffffffff is 32 1s
        if num == 0:
            return "0"
        
        s={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,
        9:9,10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res=''
        num &= 0xffffffff #condition is to limit num to 32 bits
        while num>0:
            a=num//16
            b=num%16
            res=str(s[b])+res
            num=a
        
        return res