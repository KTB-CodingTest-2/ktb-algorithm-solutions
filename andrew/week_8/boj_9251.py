import sys

def input():
    return sys.stdin.readline().strip()

str1 = input()
str2 = input()

LCS = []

for i in range(len(str1)):
    LCS.append([])
    for j in range(len(str2)):
        LCS[i].append(0)
        # if i == 0 or j == 0:
        #     LCS[i][j] = 0
        if str1[i] == str2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = 0

print(f"  {' '.join(str2)}")
for idx, line in enumerate(LCS):
    print(str1[idx], *line)