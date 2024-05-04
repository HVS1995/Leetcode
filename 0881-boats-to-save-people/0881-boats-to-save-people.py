class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n =len(people)
        boat = 0
        people.sort()
        i,j = 0, n-1
        while i <= j:
            if people[j]+people[i] <= limit:
                i += 1 
                j -= 1
                boat +=1
            else:
                j -=1
                boat += 1 
                
        return boat
        