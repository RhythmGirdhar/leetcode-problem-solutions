from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_hash = Counter(arr)
        key_list = []
        for key,val in count_hash.items():
            if val == 1:
                key_list.append(key)

        if len(key_list) >= k:
            return key_list[k-1]
        return ""