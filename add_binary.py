#https://leetcode.com/problems/add-binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m=len(a)
        n=len(b)
        max_l=max(len(a),len(b))
        a=a.zfill(max_l)
        b=b.zfill(max_l)
        summ=0
        carry=0
        strsum=""
        for i in range(len(a)-1,-1,-1):
            summ=int(a[i])+int(b[i])+carry
            carry=summ//2
            write=summ%2
            strsum= str(write)+strsum
        if carry:
            strsum = '1' + strsum
        return strsum