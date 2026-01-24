class Solution:
    def firstUniqChar(self, s: str) -> int:

        strings={}
        for char in s:
            if char in strings:
                strings[char]+=1
            else:
                strings[char]=1
        
        for i in range(0,len(s)):
            if strings[s[i]]==1:
                return i

        return -1


            

    
        


    


      
        

        

                
        
        