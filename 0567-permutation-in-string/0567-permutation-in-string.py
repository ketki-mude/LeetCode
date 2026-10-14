class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        s1_count={}
        window_count={}

        for char in s1:
            if char in s1_count:
                s1_count[char]+=1
            
            else:
                s1_count[char]=1


        left=0

        for right in range(len(s2)):

            char=s2[right]

            if char in window_count:
                window_count[char]+=1
            else:
                window_count[char]=1

            if right-left+1>len(s1):
                       
                if s2[left] in window_count:
                    if window_count[s2[left]]>1:

                        window_count[s2[left]]-=1
                    else:
                        del window_count[s2[left]]

                left+=1

            if s1_count==window_count:
                return True

        return False





        


            

            
        



        