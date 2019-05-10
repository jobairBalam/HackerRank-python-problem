n = int(input().strip())
candles = list(map(int,input().strip().split(' ')))

print(candles.count(max(candles)))
