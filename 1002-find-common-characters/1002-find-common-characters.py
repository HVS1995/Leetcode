class Solution:
    def countarray(slef,words,count):
        for ch in words:
            count[ord(ch) - ord('a')] += 1
            
            
            
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        n = len(words)
        count = [0]*26
        self.countarray(words[0],count)
        
        for i in range(1, n):
            temp = [0] * 26
            self.countarray(words[i], temp)
            
            
            for j in range(26):
                count[j] = min(count[j], temp[j])
        
        
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a'))] * count[i])
        
        return result
        
        