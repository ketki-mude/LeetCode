class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)  
        numbers = {}
        for i in range(0, n):
            numbers[nums[i]] = i
       
        print(numbers)
        for i in range(0, n):
            key = target - nums[i]

            if key in numbers:
                if numbers[key]!=i:
                    return [i, numbers[key]]
               
                
