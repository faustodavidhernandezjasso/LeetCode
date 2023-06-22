class Solution:

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        t_n = 0
        t_n1 = 1
        t_n2 = 1
        for i in range(3, n + 1):
            result = t_n + t_n1 + t_n2
            t_n = t_n1
            t_n1 = t_n2
            t_n2 = result
        return result
        # T = [0, 1, 1]
        # if (n <= 2):
        #     return T[n]
        # for i in range(3, n + 1):
        #     T.append(T[i - 3] + T[i - 2] + T[i - 1])
        # return T[n]
    

if __name__ == '__main__':
    n = 25
    s = Solution()
    print(s.tribonacci(25))