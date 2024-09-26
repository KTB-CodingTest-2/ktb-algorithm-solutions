def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        line = bin(i|j)[2:].replace("1", "#").replace("0"," ")
        if len(line) < n:
            line = " " * (n - len(line)) + line
        answer.append(line)
    return answer