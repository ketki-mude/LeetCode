class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_dict = {}
        nums2_dict={}

        for num in nums1:
            # if num in nums1_dict:
            nums1_dict[num]=None
        #print(nums1_dict)

        for num in nums2:
            # if num in nums1_dict:
            nums2_dict[num]=None
        #print(nums2_dict)


        returned_list=[]

        for key in nums1_dict:
        # Check if key exists in the second AND the values match
            if key in nums2_dict and nums1_dict[key] == nums2_dict[key]:
                returned_list.append(key)
        
        return returned_list

            

        