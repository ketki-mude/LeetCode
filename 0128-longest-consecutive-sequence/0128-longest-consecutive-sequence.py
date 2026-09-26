class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        sorted_array=sorted(nums)
        n=len(sorted_array)

        count=1
        longest=1

        if not nums:
            return 0
        for i in range(0,n-1):
            if sorted_array[i]==sorted_array[i+1]:
                continue

            if sorted_array[i+1]==sorted_array[i]+1:
                count+=1
            
            else:
                count=1
        
            longest=max(longest,count)

        return longest
            
        
        
        


        