#https://leetcode.com/problems/crawler-log-folder/
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        op=0
        for i in range(len(logs)):
            if logs[i]=='./':
                pass
            elif logs[i]=='../':
                op=max(0,op-1)
            else:
                op=op+1
        if op<0:
            return 0
        return op