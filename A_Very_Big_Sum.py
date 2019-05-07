n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
sum=0
for i in range(n):
    sum = sum + arr[i]
print(sum)
