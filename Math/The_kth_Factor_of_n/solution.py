class Solution:

    def kthFactor(self, n: int, k: int) -> int:
        c = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                c += 1
                if (c == k):
                    return i
        return -1
    

if __name__ == '__main__':
    s = Solution()
    k = 2
    n = 7
    print(s.kthFactor(n, k))