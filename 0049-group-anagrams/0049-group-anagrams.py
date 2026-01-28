class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        unique_dict={}
        for ele in strs:
            sort_element = "".join(sorted(ele))
            if sort_element not in unique_dict:
                unique_dict[sort_element] = [ele]
            else:
                unique_dict[sort_element].append(ele)

        #print(unique_dict)
        return_list = []
        for key in unique_dict:
            return_list.append(unique_dict[key])

        #print(return_list)
        return return_list
            




        
        