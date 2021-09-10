def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for target_len in range(1, len(s) // 2 + 1):
        target = s[:target_len]
        count = 1
        compressed = ''

        for i in range(target_len, len(s), target_len):
            check = s[i: i + target_len]

            if target == check:
                count += 1
            else:
                if count == 1:
                    count = ''
                compressed += (str(count) + target)
                target = check
                count = 1

        if count == 1:
            count = ''
        compressed += (str(count) + target)
        answer.append(len(compressed))

    return min(answer)
