class Solution(object):
    """
    Two Sum
    Given an array of integers, return indices of the two numbers
    such that they add up to a specific target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.Example:
    Given nums = [2, 7, 11, 15], target = 22,
    Because nums[3] + nums[1] = 15 + 7 = 22,
    return [3, 1].
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # time complexity O(n**2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])
                    return [i, j]
        return None


# test
nums = [2, 7, 11, 15]
target = 22
sol = Solution()

print(sol.twoSum(nums, target))
