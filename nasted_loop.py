li = []
scores = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    tmp = [name, score]
    li.append(tmp)
    scores.append(score)
uniqueScores = list(set(scores))
uniqueScores.sort()
secondLowest = uniqueScores[1]

li.sort()

for i in li:
    if (i[1] == secondLowest):
        print(i[0])
