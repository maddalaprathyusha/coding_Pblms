#find majority element
def majority_element(nums):
    
    ele = None
    count = 0

    # Voting Algorithm
    for num in nums:
        if count == 0:
            ele = num
            count = 1
        elif num == ele:
            count += 1
        else:
            count -= 1

    return ele

input_array = [2, 1, 2]
result = majority_element(input_array)
print("Majority element:", result)
