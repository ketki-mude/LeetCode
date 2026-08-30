class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store_count={}
        
        for num in nums:
            if num not in store_count:
                store_count[num]=1

            else:
                store_count[num]+=1

        frequency = [0] * (len(nums) + 1)
        
        for num in store_count:
            count=store_count[num]
            
            if frequency[count]==0:
                frequency[count]=[num]
            else:
                frequency[count].append(num)

        print(store_count)
        print(frequency)

        returned_array=[]
        count=0
        for i in range(len(frequency)-1,0,-1):
            if count<k and frequency[i]!=0:
                returned_array.extend(frequency[i])
                count+=1

        final_array=[]
        #returned_array=[1,2,3]
        for i in range(0,k):
            final_array.append(returned_array[i])

        return final_array
     
       


    

        



        
        