# Approach: for the first 8 chars, you just add them as it is 1 * 8, then for the next 8, you do 2 * 8, for the next 8, you do 3 * 8, and so on. So we first loop them for these, then for
# the remaining characters, we count the remaining based on where in range they are present. Then we multiple them with divided by 8 + 1

class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        val = len(word) // 8
        limit = len(word) % 8
        for i in range(val + 1):
            count += 8 * i
        count += (val + 1) * limit
        return count