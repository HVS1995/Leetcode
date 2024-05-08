class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = ' '.join(reversed(words))
        return reverse
        