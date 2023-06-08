class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        t = target
        length_of_list = len(nums)
        for i in range(length_of_list):
            for j in range(i + 1, length_of_list):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))