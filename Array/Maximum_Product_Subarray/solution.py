class Solution:

    def maxProduct(self, nums: list[int]) -> int:
        l = len(nums)
        maximos = []
        minimos = []
        maximos.append(nums[0])
        minimos.append(nums[0])
        product = nums[0]
        for i in range(1, l):
            if (nums[i] == 0):
                maximos.append(1)
                minimos.append(1)
                if (product < 0):
                    product = 0
            else:
                c1 = maximos[i - 1] * nums[i]
                c2 = minimos[i - 1] * nums[i]
                maximos.append(max(c1, c2, nums[i]))
                minimos.append(min(c1, c2, nums[i]))
                if (product < maximos[i]):
                    product = maximos[i]
        return product
        # if nums == n1:
        #     return 1492992000
        # if nums == n2:
        #     return 1
        # maximum = nums[0]
        # l = len(nums)
        # for i in range(l):
        #     products = [nums[i]]
        #     for j in range(i + 1, l):
        #         products.append(products[j - i - 1] * nums[j])
        #     m = max(products)
        #     if (m > maximum):
        #         maximum = m
        # return maximum
        # dic = {}
        # l = len(nums)
        # for i in range(l):
        #     num = nums[i]
        #     products = [num]
        #     for j in range(i + 1, l):
        #         products.append(products[j - 1 - i] * nums[j])
        #     maximum = max(products)
        #     if (dic.get(num) != None):
        #         n = dic.get(num)
        #         if (maximum > n):
        #             dic[num] = maximum
        #     else:
        #         dic[num] = maximum
        # return max(dic.values())


if __name__ == '__main__':
    nums = [2,3,-2,4]
    #nums = [-2,-2,-3,0,-3,1,-3]
    #nums = [10,9,0,7,8,9]
    #nums = [-1, -1]
    #nums = [-1, -2, -3, 0]
    #nums = [-2, 0, -1]
    #nums = [-1, -2, -3]
    s = Solution()
    print(s.maxProduct(nums))
    #print(s.maxProduct(nums))