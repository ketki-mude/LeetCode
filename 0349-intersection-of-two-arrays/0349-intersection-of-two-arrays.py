class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        num_dict1={}
        num_dict2={}

        for num in nums1:
            num_dict1[num]=None
        
        for num in nums2:
            num_dict2[num]=None

        returned_list=[]

        for key in num_dict1:
            if key in num_dict2 and num_dict1[key]==num_dict2[key]:
                returned_list.append(key)
        
        return returned_list

      
        