import itertools
import sys
datalist = []
data = list()

while True:
    data = list(map(int, sys.stdin.readline().split()))

    if data[0] == 0:
        break
    
    datalist.append(data)


for data_item in datalist:
    k = data_item[0]
    s = data_item[1:]
    
    zohap = list(itertools.combinations(s, 6))
    for i in range(len(zohap)) :
        print(*zohap[i])
    if data_item != datalist[-1]:
        print('')