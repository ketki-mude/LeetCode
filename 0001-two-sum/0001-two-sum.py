class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        unique_dict={}

        for i in range(0,len(nums)):
            unique_dict[nums[i]]= i

        for i in range(0,len(nums)):
            key= target - nums[i]

            if key in unique_dict and i!= unique_dict[key]:
                return [i,unique_dict[key]]

        





            
