class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # clean_string=""
        # for char in s:
        #     if char.isalnum():
        #         clean_string+= char.lower()
        clean_s = "".join([c.lower() for c in s if c.isalnum()])
        reverse_string=clean_s[::-1]
        
        if reverse_string==clean_s:
            return True
        
        return False
    
        