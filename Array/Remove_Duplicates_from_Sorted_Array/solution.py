class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        d = {}
        for i in range(l):
            if (d.get(nums[i]) == None):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        keys = list(d.keys())
        k = len(keys)
        for i in range(k):
            nums[i] = keys[i]
        print(nums)
        return k
    
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    s.removeDuplicates(nums)