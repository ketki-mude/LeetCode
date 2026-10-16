class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        n=len(temperatures)
        result=[0]*n
        stack=[]

        for i in range(n-1,-1,-1):

            # if not stack:
            #     stack.append(i)
            #     result[i]=0

            while stack and temperatures[stack[-1]]<=temperatures[i]:  
                stack.pop()

            if stack:
                answer = stack[-1]-i
                result[i]=answer       
       
            stack.append(i)

        return result
            
                


        