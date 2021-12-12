
class QuickSort:
    def quickSort(self, nums):
        self.quickSort2(nums, 0, len(nums) -1)

    def quickSort2(self, nums, low, hi):
        if low < hi:
            p = self.partition(nums, low, hi)
            self.quickSort2(nums, low, p - 1)
            self.quickSort2(nums, p + 1, hi)

    def partition(self, nums, low, hi):
        pivotIndex = self.getPivot(nums, low, hi)
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[low] = nums[low], nums[pivotIndex]
        border = low

        for i in range(low, hi+1):
            if nums[i] < pivotValue:
                border += 1
                nums[i], nums[border] = nums[border], nums[i]

        nums[low], nums[border] = nums[border], nums[low]
        return border


    def getPivot(self, nums, low, hi):
        mid = (hi + low)//2
        pivot = hi
        if nums[low] < nums[mid]:
            if nums[mid] < nums[hi]:
                pivot = mid
            elif nums[low] < nums[hi]:
                pivot = low
        return pivot


if __name__ == '__main__':
    quickSort = QuickSort()
    nums = [17, 41, 5, 22, 54, 6, 29, 3, 13]
    quickSort.quickSort(nums)
    print("Quick sort :", nums)
