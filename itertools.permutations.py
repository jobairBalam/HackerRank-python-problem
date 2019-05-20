from itertools import permutations

word, num = input().split(" ")
permutations = list(permutations(word, int(num)))
permutations.sort()

for i in permutations:
    print("".join(i))
    
    
    
    
    
'''
from itertools import permutations

S = input().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print(''.join(i))
    
    
    
'''
