def makeGoodArray(count):
    global result

    for i in range(1, count//2+1):
        if result[count-i:] == result[count-2*i:count-i]:
            return
    if count == N:
        print(*result, sep='')
        exit(0)
    for i in range(1, 4):
        result.append(i)
        makeGoodArray(count+1)
        result.pop()

result = []
N = int(input())
makeGoodArray(0)