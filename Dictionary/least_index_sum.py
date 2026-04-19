class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Create dictionaries to store indices
        d1={}
        d2={}
        s=0
        result=float('inf')
        lst=[]
        # Build index mappings for both lists
        for idx,val in enumerate(list1):
            d1[val]=idx
        for idx,val in enumerate(list2):
            d2[val]=idx
        print(f"Dictionaries are {d1} and {d2}")
        # Find restaurants with minimum index sum
        for x in d1.keys() & d2.keys() :
            
            s=d1[x]+d2[x]
            if s<result:
                result=s
                lst=[x]
            elif s==result:
                lst.append(x)
        print(f"List is {lst}, ")
        return lst