class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        max_length=0
        visited_element= set()

        for right in range(len(s)):

            while s[right] in visited_element:
                visited_element.remove(s[left])
                left+=1
            
            visited_element.add(s[right])

            max_length= max(max_length, right-left+1)

        return max_length


        