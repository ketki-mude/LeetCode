class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unique_dict={}

        for word in strs:
            freq_array=[0]*26
            for letters in word:
                index = (ord(letters)-ord("a"))-1
                freq_array[index]+=1
            
            freq_tuple= tuple(freq_array)
            
            if freq_tuple not in unique_dict:
                unique_dict[freq_tuple] = [word]
            else:
                unique_dict[freq_tuple].append(word)

        #print(unique_dict)
        return_list = []
        for key in unique_dict:
            return_list.append(unique_dict[key])

        #print(return_list)
        return return_list
            




        
        