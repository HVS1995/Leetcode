from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]  # Return a list with an empty string to signify a valid path
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sentence in backtrack(end):
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)
        