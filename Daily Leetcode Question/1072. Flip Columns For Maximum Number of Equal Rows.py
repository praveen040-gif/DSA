from collections import Counter
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_counts = Counter()
        # print(type(pattern_counts))

        for row in matrix:
            pattern_list = []
            first_element = row[0]
            for i in range(len(row)):
                flipped_value = row[i] ^ first_element
                pattern_list.append(flipped_value)
            # print(pattern_list)
            pattern = tuple(pattern_list)
            pattern_counts[pattern] += 1
        return max(pattern_counts.values())
