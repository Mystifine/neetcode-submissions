class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [];
        
        for index in range(len(nums)):
            for secondIndex in range(index+1, len(nums)):
                if nums[index] + nums[secondIndex] == target:
                    output.append(index);
                    output.append(secondIndex);
                    return output;
        return output;