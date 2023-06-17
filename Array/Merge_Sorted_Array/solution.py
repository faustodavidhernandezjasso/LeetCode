class Solution:

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if (n == 0):
            return
        elif (m == 0):
            nums1 = nums2
        else:
            i = n - 1
            j = m - 1
            k = m + n - 1
            while (i >= 0 and j >= 0 and k >= 0):
                if nums1[j] < nums2[i]:
                    nums1[k] = nums2[i]
                    k -= 1
                    i -= 1
                else:
                    nums1[k] = nums1[j]
                    j -= 1
                    k -= 1
            if (i >= 0):
                for a in range(i+1):
                    nums1[a] = nums2[a]
        

if __name__ == '__main__':
    # nums1 = [1,2,3,0,0,0] 
    # m = 3 
    # nums2 = [2,5,6] 
    # n = 3
    # nums1 = [0] 
    # m = 0 
    # nums2 = [1] 
    # n = 1
    # nums1 = [2,0]
    # m = 1
    # nums2 = [1]
    # n = 1
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
