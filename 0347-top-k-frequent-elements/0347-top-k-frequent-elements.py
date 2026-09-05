class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count={}

        for num in nums:
            if num in dict_count :
                dict_count[num]+=1
            else:
                dict_count[num]=1
        
        freq = [None]*(len(nums)+1)

        for key in dict_count:
            index=dict_count[key]
            if freq[index] is None:
                freq[index]=[key]
            else:
                freq[index].append(key)

        print(freq)
        print(dict_count)

        returened_list=[]

        for i in range(len(freq)-1,0,-1):
            if freq[i]==None:
                continue
            else:
                if len(returened_list) <= k:
                    returened_list.extend(freq[i])
                else:
                    break
                
        return returened_list[:k]


                    



            



        