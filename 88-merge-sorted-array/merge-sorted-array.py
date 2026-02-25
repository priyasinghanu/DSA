class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        i = m - 1          # nums1 ka last valid element
        j = n - 1          # nums2 ka last element
        k = m + n - 1      # nums1 ka last index
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Agar nums2 ke elements bach gaye ho
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1