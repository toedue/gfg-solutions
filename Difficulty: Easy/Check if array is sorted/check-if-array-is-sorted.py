class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        
        ptr1 = 0
        ptr2 = 1
        
        while(ptr2 < len(arr)):
            if arr[ptr1] > arr[ptr2]:
                return False
                
            ptr1 += 1
            ptr2 += 1
                
        return True
            
        
            