from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        a = [pref[0]]
        for i in range(1, len(pref)):
            a.append(pref[i] ^ pref[i - 1])

        return a
