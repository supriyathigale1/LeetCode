class Solution:
    def addstrings(self, num1: str, num2: str) -> str:
        max_l=max(len(num1),len(num2))
        num1=num1.zfill(max_l)
        num2=num2.zfill(max_l)
        carry=0
        summ=0
        res=""
        for i in range(len(num1)-1,-1,-1):
            summ=int(num1[i])+int(num2[i])+carry
            carry=summ//10
            digit=(summ)%10
            res=str(digit)+res
        if carry:
            res = str(carry) + res
        if num1=='0' and num2=='0':
            return '0'
        return res
