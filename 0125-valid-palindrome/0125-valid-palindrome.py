class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_string = ""
        for char in s:
            if char.isalnum():
                clean_string+=char.lower()

        print(clean_string)

        reverse_clean_string= clean_string[::-1]

        print(reverse_clean_string)

        if clean_string==reverse_clean_string:
            return True
        
        return False

        

        
        