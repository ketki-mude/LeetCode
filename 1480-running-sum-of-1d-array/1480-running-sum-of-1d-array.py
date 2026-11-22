class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        n=len(nums)
        result=[1]*n

        prefix_sum=0
        for i in range(0,n):
            prefix_sum+=nums[i]
            result[i]=prefix_sum

        return result

        