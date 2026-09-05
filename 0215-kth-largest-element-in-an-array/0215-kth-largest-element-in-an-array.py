import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        returned_list=[]

        for num in nums:
            heapq.heappush(returned_list,num)

            if len(returned_list)>k:
                heapq.heappop(returned_list)

        return returned_list[0]





        