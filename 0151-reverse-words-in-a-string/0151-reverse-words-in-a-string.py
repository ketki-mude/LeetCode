class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        i=0
        j=len(words)-1

        while i<j:
            temp=words[i]
            words[i]=words[j]
            words[j]=temp

            i+=1
            j-=1

        result=" ".join(" ".join(words).split())
        return result




     
        
            

      

        

        