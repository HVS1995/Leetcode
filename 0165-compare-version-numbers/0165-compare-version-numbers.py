class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revision1 = version1.split('.')
        revision2 = version2.split('.')
        length = max(len(revision1),len(revision2))
        for i in range(length):
            rev1 = int(revision1[i])  if  i < len(revision1) else 0 
            rev2 = int(revision2[i])  if  i < len(revision2) else 0 
            
            if rev1 < rev2:
                return -1
            if rev1 > rev2:
                return 1
            
        return 0