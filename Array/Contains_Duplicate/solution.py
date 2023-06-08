class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        l = len(nums)
        for i in range(l):
            if (d.get(nums[i]) == None):
                d[nums[i]] = 1
            else:
                return True
        return False
        
if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    s = Solution()
    print(s.containsDuplicate(nums))