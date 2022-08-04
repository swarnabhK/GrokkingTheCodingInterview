# find the maximum sum subarray.
#[2,1,5,1,3,2,8]: 012, 123
# 215: 8, 151: 7, 513: 9, 132: 6, max is 9


#Brute force method.
def maximumSumSubarrayBrute(arr,k):
  max_n = arr[0]
  windowSum = 0
  for i in range(len(arr)-k+1):
    windowSum = 0
    for j in range(i,i+k):
      windowSum+=arr[j]  
    max_n = max(max_n,windowSum)
  return max_n


maximumSumSubarrayBrute([2,1,5,1,3,2],3)


# use sliding window pattern.
#windows: 215, windowsum = 7, remove 2, window 151: windowSum - 7
def maximumSumSubarray(arr,k):
  max_sum = arr[0]
  windowSum,windowStart = 0,0
  for i in range(len(arr)):
    windowSum+=arr[i]
    if(i>=k-1):
      max_sum = max(windowSum,max_sum)
      windowSum-=arr[windowStart]
      windowStart+=1
  return max_sum

print(maximumSumSubarray([2,1,5,1,3,2,9],3))

