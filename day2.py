class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            # Checking a set takes O(1) time
            if num in seen:
                return True
            seen.add(num)
            
        return False



#idk what
from collections import Counter

def findMinOperations(centers):
    n= len(centers)

    freq=Counter(centers)
    mx=max(freq.value())

    if n-mx<mx:
        return mx
    
    return n+1//2


