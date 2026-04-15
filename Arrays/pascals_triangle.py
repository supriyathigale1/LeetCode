#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        k=0
        for x in range(numRows):
            if x ==0:
                lst.append([1])
            elif x ==1:
                lst.append([1,1])
            else:
                k=0
                l=[1]
                while k<len(lst[x-1])-1:
                    l.append(lst[x-1][k]+lst[x-1][k+1])
                    k=k+1
                l.append(1)
                lst.append(l)
                
        print(lst)
        return lst

