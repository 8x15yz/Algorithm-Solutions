class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, target, fs, ed):
            mid = ((ed-fs)//2)+fs
            if nums[mid] == target:
                return mid
            elif len(nums[fs:ed+1]) <= 2:
                for num in range(fs, ed+1):
                    if target <= nums[num]:
                        return num
                else:
                    return ed+1
                        
            if target > nums[mid]:
                return(binarysearch(nums, target, mid+1, ed))
            else:
                return(binarysearch(nums, target, fs, mid))
                
                
        return (binarysearch(nums, target, 0, len(nums)-1))
