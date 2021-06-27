def hourglassSum(arr):
    sum = []
    rowlen = len(arr[0])
    columlen = len(arr)
    for row in range(rowlen - 2):
        for col in range(columlen - 2):
            a = arr[row][col]
            b = arr[row][col + 1]
            c = arr[row][col + 2]
            d = arr[row + 1][col + 1]
            e = arr[row + 2][col]
            f = arr[row + 2][col + 1]
            g = arr[row + 2][col + 2]
            sum.append(a + b + c + d + e + f + g)
    return max(sum)
