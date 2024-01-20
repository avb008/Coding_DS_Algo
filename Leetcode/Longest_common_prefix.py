from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_length = min([len(s) for s in strs])
        prefix = ""
        for i in range(prefix_length + 1):
            target = strs[0][:i]
            count = 0
            for s in strs:
                if s[:i] != target:
                    return prefix
                else:
                    count += 1

            if count == len(strs):
                prefix = target

        return prefix


if __name__ == "__main__":
    obj = Solution()
    print(obj.longestCommonPrefix(["flower", "flow", "flight"]))
    print(obj.longestCommonPrefix(["dog", "racecar", "car"]))
    print(obj.longestCommonPrefix(["ab", "a"]))
    print(obj.longestCommonPrefix(["a"]))
    print(obj.longestCommonPrefix(["ab", "ab", "ab"]))
