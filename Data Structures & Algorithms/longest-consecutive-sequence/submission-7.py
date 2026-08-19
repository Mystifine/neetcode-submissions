class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        longest = 1
        counter = 1

        uniqueNums = list(set(nums))
        nums = sorted(uniqueNums)
        print(nums)

        for i in range(0, len(nums)):
            val = nums[i]
            if (i+1) < len(nums):
                nextVal = nums[i+1]
                if (nextVal-1 == val):
                    counter += 1
                else:
                    longest = counter > longest and counter or longest
                    counter = 1
        longest = counter > longest and counter or longest
        return longest