import random
class InsertionSorting:

    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                else:
                    break

    def insertionSort2(self, nums):
        for i in range(1, len(nums)):
            j = i - 1
            while nums[j] > nums[j+1] and j >= 0:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1

    def insertionSortWithShift(self, nums):
        for i in range(1, len(nums)):
            curNum = nums[i]
            for j in range(i-1, -1, -1):
                if nums[j] > curNum:
                    nums[j+1] = nums[j]
                    nums[j] = curNum
                else:
                    nums[j+1] = curNum
                    break



if __name__ == '__main__':
    insertionSorting = InsertionSorting()
    numArray = [7, 8, 5, 4, 9, 2]
    insertionSorting.insertionSortWithShift(numArray)
    print("Sorted Array: ", numArray)