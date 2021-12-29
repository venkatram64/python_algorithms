class Majority(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNumDict = {}
        for num in nums:
            if num in myNumDict.keys():
                value = myNumDict[num]
                value += 1;
                myNumDict[num] = value
            else:
                myNumDict[num] = 1

        majority = len(nums) / 2

        for key, value in myNumDict.items():
            if value > majority:
                return key


if __name__ == '__main__':
    majority = Majority()
    num = majority.majorityElement([2,2,1,1,1,2,2])
    print(num)