arr = list(map(int, input().strip().split(' ')))
Min = sum(arr) - max(arr)
Max = sum(arr) - min(arr)
print(Min,Max)
