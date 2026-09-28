class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        max_lenght=0
        substring=set()

        for right in range(len(s)):
            if s[right] not in substring:
                substring.add(s[right])
            
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left+=1

                substring.add(s[right])
        
            max_lenght=max(max_lenght, right-left+1)
        
        return max_lenght

        