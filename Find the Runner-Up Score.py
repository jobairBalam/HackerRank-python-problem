n = int(input("Enter the length"))
num = map(int, input().split())
print(count(list(set(num)))[-2])
