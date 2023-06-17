class Solution:

    def lengthOfLIS(self, nums: list[int]) -> int:
        l = len(nums)
        result = [1] * l
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1 + result[j])
        return max(result)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    s = Solution()
    print(s.lengthOfLIS(nums))
