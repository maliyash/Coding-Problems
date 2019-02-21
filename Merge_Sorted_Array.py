class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        i = 0
        j= 0
        l = []
        k = 0
        nums3 = nums1.copy() 
        while(i<m and j<n):
            
            if(nums3[i] <= nums2[j]):
                nums1[k] = nums3[i]
                i = i +1
                
                
            else:
                nums1[k] = nums2[j]
                j = j +1
            k = k + 1
            
        while(i<m):
            nums1[k] = nums3[i]
            i = i +1
            k = k +1
        
        while(j<n):
            nums1[k] = nums2[j]
            j = j +1
            k = k + 1