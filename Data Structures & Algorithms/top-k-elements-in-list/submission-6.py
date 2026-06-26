class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [];
        countedNumbers = {};
        for num in nums:
            countedNumbers[num] = (countedNumbers.get(num) or 0) + 1;
        print(countedNumbers)
        for _ in range(k):
            
            mostFreqNum, mostFreqNumCount = None, 0;
            for num, count in countedNumbers.items():
                if mostFreqNum == None or count > mostFreqNumCount:
                    mostFreqNum = num;
                    mostFreqNumCount = count;
                    print(mostFreqNum, mostFreqNumCount)
            countedNumbers[mostFreqNum] = 0;

            output.append(mostFreqNum)
        return output