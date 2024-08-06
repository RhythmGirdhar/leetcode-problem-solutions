# Approach: First I get the occurrence of each character in the string. If the number of characters is <= 8, I can just assign all of them to be the first character on phone and count all values
# However, issue comes when there are more than 8, then we need to use the most occuring ones first. So, I sort them in desc order and then go over, if I have already finished 8 values, I will 
# go to the next and assign second char on tab, then third and so on. 

from collections import Counter
from collections import OrderedDict
class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        distinct_hash = Counter(word)
        sorted_hash = OrderedDict(sorted(distinct_hash.items(), key=lambda kv:kv[1], reverse=True))
        internal_count = 0
        for k,v in sorted_hash.items():
            # limit = internal_count // 7
            # val = internal_count % 7
            if internal_count < 8:
                count += v
            elif internal_count >= 8 and internal_count < 16:
                count += v + v
            elif internal_count >= 16 and internal_count < 24:
                count += v + v + v
            else:
                count += v + v + v + v
            internal_count += 1
        
        return count
        