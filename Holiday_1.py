def addOne(digits):
    # Start from the rightmost digit
    n = len(digits)
    carry = 1
    
    for i in range(n - 1, -1, -1):
        # Add the carry to the current digit
        current_sum = digits[i] + carry
        # Update the digit and reset carry
        digits[i] = current_sum % 10
        carry = current_sum // 10

    # If there is still a carry, insert it at the beginning
    if carry:
        digits.insert(0, carry)

    return digits

# Example usage
input_array = [1, 2, 3]
output_array = addOne(input_array)
print("Input:", input_array)
print("Output:", output_array)
