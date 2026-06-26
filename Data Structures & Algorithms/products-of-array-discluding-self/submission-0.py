class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums);

        for i in range(len(nums)):
            product = 1;
            for k in range(len(nums)):
                if i != k:
                    product *= nums[k]
            output[i] = product
        return output