class Solution:

    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        array = [0] * (2 * n)
        for i in range(n):
            array[i] = nums[i]
            array[i + n] = nums[i]
        return array

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,2,1]
    array = s.getConcatenation(nums)
    print(array)