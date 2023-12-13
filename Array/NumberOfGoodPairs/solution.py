class Solution:

    def numIdenticalPairs(self, nums: list[int]) -> int:
        l = len(nums)
        goodPairs = 0
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] == nums[j]:
                    goodPairs += 1
        return goodPairs

    def numIdenticalPairsOptimal(self, nums: list[int]) -> int:
        goodPairs = 0
        count = {}
        for n in nums:
            if n in count:
                goodPairs += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return goodPairs
                

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1]
    result = s.numIdenticalPairsOptimal(nums)
    print(result)