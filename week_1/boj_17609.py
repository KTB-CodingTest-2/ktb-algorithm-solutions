n = int(input())

def isit_aplindrome(a):
    count = 0
    start = 0
    end = len(a)-1

    spot = 0

    while end >= start:
        if a[start] == a[end]:
            end -= 1
            start += 1
        else:
            if start <= end - 1:
                aplindrome = a[:end] + a[end+1:]
                if aplindrome[:] == aplindrome[::-1]:
                    return 1
            if start + 1 <= end:
                aplindrome = a[:start] + a[start+1:]
                if aplindrome[:] == aplindrome[::-1]:
                    return 1
            return 2
        
    return 0

text = list()
for i in range(n):
    text.append(input())

for i in range(n):
    print(isit_aplindrome(text[i]))