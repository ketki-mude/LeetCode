class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        s_dict={}
        t_dict={}

        for char in s:
            if char in s_dict:
                s_dict[char]+=1
            else:
                s_dict[char]=1

        print(s_dict)

        for char in t:
            if char in t_dict:
                t_dict[char]+=1
            else:
                t_dict[char]=1

        print(t_dict)

    

        for char in s_dict:
            if char in t_dict:
                if s_dict[char]!=t_dict[char]:
                    return False
            else:
                return False
            
        return True

    






        