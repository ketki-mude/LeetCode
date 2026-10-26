import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        low=1
        high=max(piles)
        current_mid=0

        while low<=high:

            mid=(low+high)//2
            time = 0

            for pile in piles:
                time+= math.ceil(pile/mid)

            if time>h:
                low=mid+1
            else:
                current_mid=mid
                high=mid-1

        return current_mid


            
            




















     