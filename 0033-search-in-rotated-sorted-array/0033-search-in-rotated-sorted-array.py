class Solution:
    def search(self, nums: list[int], target: int) -> int:

        low=0
        high=len(nums)-1

        while low <= high:

            mid=(low+high)//2
            
            if target==nums[mid]:
                return mid

            if nums[low]<=nums[mid]: # left part is sorted

                if nums[low]<=target and target<=nums[mid]:
                    high=mid-1
                
                else:
                    low=mid+1

            elif nums[mid]<=nums[high]: # right part is sorted

                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return -1










        