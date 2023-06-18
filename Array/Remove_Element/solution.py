class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        indixes1 = []
        indixes2 = []
        l = len(nums)
        c = 0
        for i in range(l):
            if nums[i] == val:
                indixes1.append(i)
                c += 1
            else:
                indixes2.append(i)
                continue
        k = len(indixes2)
        l1 = len(indixes1)
        new_indixes = list(filter(lambda x: x >= k, indixes2))
        c_new = 0
        for i in range(l1):
            if (indixes1[i] < k):
                self.swap(nums, indixes1[i], new_indixes[c_new])
                c_new += 1
        return k
    
    def swap(self, nums: list[int], i: int, j: int) -> None:
        if (i == j):
            return
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

if __name__ == '__main__':
    # nums = [3,2,2,3] 
    # val = 3
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))
    print(nums)
