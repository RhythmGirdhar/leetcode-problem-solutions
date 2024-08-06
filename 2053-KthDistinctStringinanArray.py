#Approach: I get the freq of occurrence of all strings in this list. I directly add the ones which are distinct. Then if k value is > the length of distinct elements, I return "" else 
# I return the k th element in the list - 1 since list is 0 indexed 

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