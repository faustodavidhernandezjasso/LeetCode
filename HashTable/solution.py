class Solution:

    def partitionString(self, s: str) -> int:
        minumum_partion = []
        partition = ""
        for ch in s:
            if partition.find(ch) >= 0:
                minumum_partion.append(partition)
                partition = ""
                partition += ch
            else:
                partition += ch
        if partition != "":
            minumum_partion.append(partition)
        return len(minumum_partion)
    

if __name__ == '__main__':
    s = "ssssss"
    sol = Solution()
    print(sol.partitionString(s))