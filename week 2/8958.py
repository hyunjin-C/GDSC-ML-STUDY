n = int(input())

for i in range(n):
    score = input()
    cnt = 0
    result = 0

    for i in range(len(score)):
        if score[i] == 'O':
            cnt += 1
            result += cnt

        else:
            cnt = 0

    print(result)
