class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        returned_array=[]
        for interval in intervals:
            start=interval[0]
            end=interval[1]

            if not returned_array:
                returned_array.append([start,end])

            else:
                current_end=returned_array[-1][1]
                next_start=start
                next_end=end

                if current_end>=next_start:
                    current_end=max(current_end,next_end)
                    returned_array[-1][1]=current_end

                else:
                    returned_array.append([start,end])

        return returned_array


