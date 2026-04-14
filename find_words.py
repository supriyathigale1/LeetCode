#https://leetcode.com/problems/keyboard-row/
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = 'qwertyuiop'
        s = 'asdfghjkl'
        t = 'zxcvbnm'
        
        i = 0
        res = []

        while i < len(words):
            w = words[i].lower()
            
            changed_j = True
            changed_k = True
            changed_m = True
            
            j = 0
            while j < len(w):
                if w[j] not in f:
                    changed_j = False
                j += 1
            
            k = 0
            while k < len(w):
                if w[k] not in s:
                    changed_k = False
                k += 1
            
            m = 0
            while m < len(w):
                if w[m] not in t:
                    changed_m = False
                m += 1
            
            if changed_j or changed_k or changed_m:
                res.append(words[i])
            
            i += 1
        
        return res