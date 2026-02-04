class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique_char={}
        right=0
        left=0
        max_count= 0

        
        while right<len(s):
            while s[right] in unique_char:
                unique_char.pop(s[left])
                left+=1

            unique_char[s[right]]=None
            max_count= max(max_count,(right-left)+1)
            right+=1
        
        return max_count

        
           
        


        

        
        