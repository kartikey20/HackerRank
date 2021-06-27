_, d = map(int, input().split())
arr = input().split()
moveToEnd = arr[:d]
del arr[:d]
print(" ".join(arr + moveToEnd))
