"""1013. Partition Array Into Three Parts With Equal Sum
Easy

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

 

Constraints:

    3 <= A.length <= 50000
    -10^4 <= A[i] <= 10^4

"""
def main(A):
    if sum(A) % 3 != 0:
        return False
    else:
        Sum = sum(A) // 3
        #print(Sum)
        tempi = 0
        for i in range(len(A) - 2):
            tempi += A[i]
            if (tempi == Sum and sum(A[i+1:]) == (2*Sum)):
                #print(A[i], i)
                tempj = 0
                for j in range(i+1, len(A) - 1):
                    tempj += A[j]
                    if (tempj == Sum and sum(A[j+1:]) == Sum):
                        #print(i, j)
                        return True
        return False

print(main(A = [0,2,1,-6,6,-7,9,1,2,0,1]))
print(main(A = [0,2,1,-6,6,7,9,-1,2,0,1]))
print(main(A = [3,3,6,5,-2,2,5,1,-9,4]))
print(main(A = [6, 1, 1, 13, -1, 0, -10, 20]))
print(main(A = [1, -1, 1, -1]))