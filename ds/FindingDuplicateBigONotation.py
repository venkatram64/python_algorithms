'''
time = a * n ^ 2 + b ==> O(n ^ 2) which is the time complexity

for binary search
iteration k = n/2^k
1 = n/2^k
n=2^k
log2 n = log2 2^k
log2 n = k * log2 2
log2 n = k
k = logn
k = O(log n)

eg: 4,9,15,21,34,57,68,91 ==> to find 68, need 3 halves
for binary search

k = O(log n) --> log2 8 --> log2 2 ^ 3 --> 3log2 2
k = O(3)  ==> 3 iteration

'''

def findDuplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                print(nums[i], " is a duplicate")
                break

if __name__ == '__main__':
    numbers = [3, 6, 2, 4, 3, 6, 8, 9]
    findDuplicates(numbers)