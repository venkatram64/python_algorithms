class SingleNumber(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myNumDict = {}
        for num in nums:
            if num in myNumDict.keys():
                value = myNumDict[num]
                value += 1
                myNumDict[num] = value
            else:
                myNumDict[num] = 1

        for key, value in myNumDict.items():
            if value == 1:
                return key



if __name__ == '__main__':
    sn = SingleNumber()
    num = sn.singleNumber([1,2,3,2,3])
    print(num)