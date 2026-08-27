class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums={}

        for num in nums:
            unique_nums[num]= None
        
        if len(nums)==len(unique_nums):
            return False
        else:
            return True
         


      