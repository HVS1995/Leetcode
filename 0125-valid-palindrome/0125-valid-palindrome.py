class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        if s == " ":
            return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                return False

        return True
                
            
            
        