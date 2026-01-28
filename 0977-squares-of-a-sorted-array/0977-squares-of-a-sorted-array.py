class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_array=[]

        for num in nums:
            sq= num **2
            squared_array.append(sq)
              
        squared_array.sort()
        return squared_array
        
        