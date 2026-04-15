class Solution:
    def my_reorderSpaces(self, text: str) -> str:
        space=text.count(' ')
        words=text.split()
        n=len(words)
        if n == 1:
            return words[0] + ' ' * space
        gap=space//(n-1)
        gap2=space%(n-1)
        k=0
        newstr=""
        for i in range(len(words)):
            newstr=newstr+words[i]
            if i!=n-1:
                k=0
                while k<gap:
                    newstr=newstr+' '
                    k=k+1
        
        while gap2>0:
            newstr=newstr+' '
            gap2=gap2-1
        return newstr
            
        



