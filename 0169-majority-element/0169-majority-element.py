class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_element={}
        max_number=8
        max_count=0
        

        for num in nums:
            if num in count_element:
                count_element[num]+=1
            else:
                count_element[num]=1

        for num in count_element:
            count = count_element[num]
            if count > max_count:
                max_count=count
                max_num=num
        
        return max_num




        
        
        
        
        



        