def parse_list_strings(arr):
    if arr == "[]":
        return []
    return list(map(int, arr.strip('[]').split(',')))

T = int(input())

for _ in range(T):
    count = 0
    p = input()
    n = int(input())
    arr = parse_list_strings(input())
    
    for i in p:
        if i == 'R':
            count += 1
        elif i == 'D':
            if not arr:
                print('error')
                break
            if count % 2 == 0:
                arr.pop(0)
            else:
                arr.pop(-1)
    else:
        if count % 2 != 0:
            arr.reverse()
        print(f"[{','.join(map(str, arr))}]")
