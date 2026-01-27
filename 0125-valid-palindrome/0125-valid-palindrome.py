class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_string=""
        for char in s:
            if char.isalnum():
                clean_string+= char.lower()
        
        reverse_string=clean_string[::-1]
        
        if reverse_string==clean_string:
            return True
        
        return False
    
        