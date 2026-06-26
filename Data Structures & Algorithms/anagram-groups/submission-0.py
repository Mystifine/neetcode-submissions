class Solution:
    def isAnagram(self, str1 : str, str2 : str) -> bool:
        str1Data = {};
        str2Data = {};
        for c in str1:
            str1Data[c] = (str1Data.get(c) or 1) + 1

        for c in str2:
            str2Data[c] = (str2Data.get(c) or 1) + 1

        for key, value in (str1Data.items()):
            if str2Data.get(key) != value:
                return False;

        for key, value in (str2Data.items()):
            if str1Data.get(key) != value:
                return False;

        return True;

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [];
        for string in strs:
            grouped = False;
            for i in range(len(output)):
                group = output[i];
                
                groupStr = group[0];
                if Solution.isAnagram(self, groupStr, string):
                    grouped = True;
                    output[i].append(string);
            
            if grouped == False:
                output.append([string])
        return output
                        

