class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        elements={}

        for num in nums:
            elements[num]=None

        if len(nums)==len(elements):
            return False

        return True

       
        