class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        count={}
        max_length=0

        for right in range(len(s)):
            char=s[right]

            if char in count:
                count[char]+=1
            else:
                count[char]=1

            max_freq = max(count.values())

            window_size = right-left+1

            while window_size - max_freq >k:

                count[s[left]]-=1
                left+=1
                window_size = right-left+1
            
            max_length= max(max_length,window_size)
        
        return max_length

            





        