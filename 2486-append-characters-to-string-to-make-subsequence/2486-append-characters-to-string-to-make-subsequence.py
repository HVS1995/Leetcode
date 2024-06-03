class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left, right = 0, 0
        left_len, right_len = len(s), len(t)
        total: int = right_len
        while left < left_len and right < right_len:
            if s[left] == t[right]:
                total -= 1
                right += 1
            left += 1
        return total
        