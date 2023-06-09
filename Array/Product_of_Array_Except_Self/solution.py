class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        prefix = []
        postfix = []
        for i in range(l):
            if (i == 0):
                prefix.append(1)
            else:
                prefix.append(nums[i - 1] * prefix[i - 1])
        rev = list(reversed(nums))
        for i in range(l):
            if (i == 0):
                postfix.append(1)
            else:
                postfix.append(rev[i - 1] * postfix[i - 1])
        postfix = list(reversed(postfix))
        product = []
        for i in range(l):
            product.append(prefix[i] * postfix[i])
        return product

if __name__ == '__main__':
    nums = [-1,1,0,-3,3]
    s = Solution()
    s.productExceptSelf(nums)


