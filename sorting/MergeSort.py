
class MergeSort:

    def mergeSort(self, nums):
        self.mergeSort2(nums, 0, len(nums) - 1)

    '''
    This method will divide the array upto the single element
    '''
    def mergeSort2(self, nums, first, last):
        if first < last:
            middle = (first + last) // 2
            self.mergeSort2(nums, first, middle)
            self.mergeSort2(nums, middle+1, last)
            self.merge(nums, first, middle, last)


    def merge(self, nums, first, middle, last):
        left = nums[first:middle+1]
        right = nums[middle+1: last+1]
        left.append(999999999)  #add arbitray big number
        right.append(999999999)  #add arbitray big number
        i = j = 0
        for k in range(first, last + 1):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1


if __name__ == '__main__':
    mergeSort = MergeSort()
    nums = [17, 87, 6, 22, 41, 3, 13, 54]
    mergeSort.mergeSort(nums)
    print("Merge sort :", nums)