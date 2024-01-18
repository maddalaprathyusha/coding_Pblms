#palindrome_integer
def is_palindrome_integer(x):
   
    if x < 0:
        return 0

    original = x
    reverse = 0

    while x != 0:
        # Pop the last digit
        digit = x % 10
        x = x // 10
        reverse = reverse * 10 + digit

    return original == reverse

input1 = 12121
output1 = is_palindrome_integer(input1)
print(f"Output for {input1}: {output1}")

input2 = 123
output2 = is_palindrome_integer(input2)
print(f"Output for {input2}: {output2}")
