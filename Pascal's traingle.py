def pascal_triangle(n):
    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

num_rows = int(input("Enter the number of rows: "))
triangle = pascal_triangle(num_rows)
for row in triangle:
    print(" " * (num_rows - len(row)), *row)
