class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k == 1:
            return [nums[0]]

        elements_count = {}

        for num in nums:
            if num in elements_count:
                elements_count[num] += 1
            else:
                elements_count[num] = 1 

        # print(elements_count)

        count_list = (len(nums)+1) * [0] # frequency list
        # print(count_list)
        for counts in elements_count:
            # print("element: ", counts, "count: ", elements_count[counts])
            if count_list[elements_count[counts]] != 0:
                count_list[elements_count[counts]].append(counts)
            else:
                count_list[elements_count[counts]] = [counts]

        # print(count_list)

        return_list = []
        
        for i in range(len(nums), -1, -1):
            if count_list[i] != 0 and k > 0:
                for num in count_list[i]:
                    return_list.append(num)
                    k -= 1

        # print(return_list)
        return return_list
        
        # print("return_list: ", return_list)




