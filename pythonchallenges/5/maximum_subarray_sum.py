
"""
This problem solved by kadane's algorithm
kadane’s algorithm and its problem-solving property to solve the “Maximum Subarray Sum” problem. We will go through the algorithm and python code for the same along with the example and its corresponding output. Lastly, we will study the time complexity of the algorithm and the real-life application of kadane’s algorithm. So, let’s get started!
"""
def maxSubArraySum(arr,size):

    max_till_now = arr[0]
    max_ending = 0

    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0


        elif (max_till_now < max_ending):
            max_till_now = max_ending

    return max_till_now

arr = [-2, -3, 4, -1, -2, 5, -3]
print("Maximum Sub Array Sum Is" , maxSubArraySum(arr,len(arr)))



