class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        merged_string= s1 + " " +s2
        list_string= merged_string.split()

        string_dict={}
        for char in list_string:
            if char in string_dict:
                string_dict[char]+=1

            else:
                string_dict[char]=1

        returned_list=[]
        for char in string_dict:
            if string_dict[char]==1:
                returned_list.append(char)

        return returned_list


        
        
    
            
            


        