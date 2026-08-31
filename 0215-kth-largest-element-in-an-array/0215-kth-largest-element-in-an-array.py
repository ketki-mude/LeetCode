import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ketu=[]
        for num in nums:
            heapq.heappush(ketu,num)

            if len(ketu)>k:
                heapq.heappop(ketu)

        return ketu[0]
            
