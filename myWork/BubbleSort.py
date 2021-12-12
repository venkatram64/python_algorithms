
class BubbleSort:

    def bubbleSort(self, nums):
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


if __name__ == '__main__':
    bubbleSort = BubbleSort()
    numArray = [7, 8, 5, 4, 9, 2]
    bubbleSort.bubbleSort(numArray)
    print("Bubble sort :", numArray)