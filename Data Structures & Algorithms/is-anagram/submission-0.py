class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sData = {};
        tData = {};
        for c in s:
            if c not in sData:
                sData[c] = 1;
            else:
                sData[c] += 1;
        
        for c in t:
            if c not in tData:
                tData[c] = 1;
            else:
                tData[c] += 1;
        
        for c in sData:
            if tData.get(c) != sData.get(c):
                return False;

        for c in tData:
            if tData.get(c) != sData.get(c):
                return False;

        return True;