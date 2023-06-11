class Solution:

    def maxProduct(self, nums: list[int]) -> int:
        dic = {}
        l = len(nums)
        for i in range(l):
            num = nums[i]
            products = [num]
            for j in range(i + 1, l):
                products.append(products[j - 1 - i] * nums[j])
            maximum = max(products)
            if (dic.get(num) != None):
                n = dic.get(num)
                if (maximum > n):
                    dic[num] = maximum
            else:
                dic[num] = maximum
        return max(dic.values())


if __name__ == '__main__':
    #nums = [2,3,-2,4]
    nums = [-2,-2,-3,0,-3,1,-3]
    #nums = [10,9,0,7,8,9]
    #nums = [-1, -1]
    s = Solution()
    print(s.maxProduct(nums))
    #print(s.maxProduct(nums))