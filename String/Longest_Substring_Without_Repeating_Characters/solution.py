class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current_length = 0
        current_str = []
        for letter in s:
            if letter in current_str:
                while letter in current_str:
                    current_str.pop(0)
                    current_length -= 1
            current_str += letter
            current_length += 1
            longest = max(longest, current_length)
        return longest
    
if __name__ == '__main__':
    #s = "dvdf"
    #s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))