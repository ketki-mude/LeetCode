class Solution:
    def firstUniqChar(self, s: str) -> int:

        frequency_string={}

        for char in s:
            if char in frequency_string:
                frequency_string[char]+=1
            else:
                frequency_string[char]=1

        print(frequency_string)
        for i in range(0,len(s)):
            if frequency_string[s[i]]==1:
                return i

        return -1








        