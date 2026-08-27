class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums= dict.fromkeys(nums, 0)
        
        if len(nums)==len(unique_nums):
            return False
        else:
            return True
         


      