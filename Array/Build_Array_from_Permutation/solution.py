class Solution:

    def buildArray(self, nums: list[int]) -> list[int]:
        l = len(nums)
        ans = [0] * l
        for i in range(l):
            ans[i] = nums[nums[i]]
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [5,0,1,2,3,4]
    print(s.buildArray(nums))