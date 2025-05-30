'''
H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
'''

class Solution:
    # def hIndex(self, citations: list[int]) -> int:
    #     hind = 0
    #     citations.sort()
    #     print(citations)
    #     for i in range(len(citations)):
    #         if citations[i] == 0:
    #             continue
    #         else:
    #             count = 0
    #             for j in range(i, len(citations)):
    #                 print(j)
    #                 if citations[j] >= citations[i]:
    #                     count += 1
    #                 if count == citations[i]:
    #                     hind = citations[i]
    #                     break
    #     return hind
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0



sol = Solution()
citations = [3,0,6,1,5]
print(sol.hIndex(citations))

citations = [1,3,1]
print(sol.hIndex(citations))

citations = [100]
print(sol.hIndex(citations))