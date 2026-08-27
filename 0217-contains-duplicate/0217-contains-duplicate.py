class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums={}

        for num in nums:
            if num not in unique_nums:
                unique_nums[num]=1
            else:
                unique_nums[num] += 1

        for num in unique_nums:
            if unique_nums[num]>1:
                return True
            else:
                continue
           
        return False

            # {2:1,14:1,18:1,22:2}
        