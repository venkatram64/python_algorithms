

class SelectionSort:

    def selection_sort(self, nums):
        for i in range(0, len(nums) - 1):
            min_index = i  #assigning index to min_index variable
            for j in range(i+1, len(nums)):  #this loop copares to find the min index
                if nums[j] < nums[min_index]:  #compare numbers and assign min index
                    min_index = j
            if min_index != i:  #swaps happened at the outer loop
                nums[i], nums[min_index] = nums[min_index], nums[i]



if __name__ == '__main__':
    numArray = [7, 8, 5, 4, 9, 2]
    selectionSort = SelectionSort()
    selectionSort.selection_sort(numArray)
    print("Selection sort : ", numArray)