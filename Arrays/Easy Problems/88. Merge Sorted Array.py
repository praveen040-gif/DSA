class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tot=m+n
        for i in range(m,tot):
            nums1[i]=nums2[m-i]
        nums1.sort()