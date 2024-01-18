#printing pascals triangle

def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []

    result = [[1]]

    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)

    return result

# Example usage:
numRows = 5
pascals_triangle = generate_pascals_triangle(numRows)

# Print the result
for row in pascals_triangle:
    print(row)
