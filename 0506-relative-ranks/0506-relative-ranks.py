class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [" " for _ in range(n)]
        mp = {}
        
        for i in range(n):
            mp[score[i]] = i
        score.sort(reverse=True)
            
        for i in range(n):
            if i == 0:  # 1st Rank athlete
                ath = mp[score[i]]
                result[ath] = "Gold Medal"
            elif i == 1:
                ath = mp[score[i]]
                result[ath] = "Silver Medal"
            elif i == 2:
                ath = mp[score[i]]
                result[ath] = "Bronze Medal"
            else:
                ath = mp[score[i]]
                result[ath] = str(i + 1)
        
        return result