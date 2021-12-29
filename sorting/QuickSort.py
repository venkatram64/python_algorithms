
class QuickSort:

    def quickSort(self, nums):
        self.quickSort2(nums, 0, len(nums) -1)

    '''
    recursion function
    17, 41, 5, 22, 54, 6, 29, 3, 13
    if startIndex < endIndex ==> if 0 < 9
    '''
    def quickSort2(self, nums, startIndex, endIndex):
        if startIndex < endIndex:  #base condition
            p = self.partition(nums, startIndex, endIndex)
            self.quickSort2(nums, startIndex, p - 1)
            self.quickSort2(nums, p + 1, endIndex)

    '''
    sorting on the basis of pivot and gives the border value
    '''
    def partition(self, nums, startIndex, endIndex):
        pivotIndex = self.getPivot(nums, startIndex, endIndex)
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[startIndex] = nums[startIndex], nums[pivotIndex]
        border = startIndex

        for i in range(startIndex, endIndex+1):
            if nums[i] < pivotValue:
                border += 1
                nums[i], nums[border] = nums[border], nums[i]

        nums[startIndex], nums[border] = nums[border], nums[startIndex]
        return border

    '''
    selecting a pivot index
    17, 41, 5, 22, 54, 6, 29, 3, 13
    mid = (17 + 13)//2 
    mid = 15 
    nums[0] < nums[9] 
    17 < 13
    ...
    ...
    pivot = endIndex(ie17)    
    '''
    def getPivot(self, nums, startIndex, endIndex):
        mid = (endIndex + startIndex)//2  # find the median of hi and low of index
        pivot = endIndex
        if nums[startIndex] < nums[mid]:
            if nums[mid] < nums[endIndex]:
                pivot = mid
            elif nums[startIndex] < nums[endIndex]:
                pivot = startIndex
        else:
            pivot = endIndex

        return pivot


if __name__ == '__main__':
    quickSort = QuickSort()
    nums = [17, 41, 5, 22, 54, 6, 29, 3, 13]
    quickSort.quickSort(nums)
    print("Quick sort :", nums)
