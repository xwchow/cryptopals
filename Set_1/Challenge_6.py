import utility
import Challenge_4

with open('6.txt', 'r') as fin:
    msg = fin.read().replace('\n', '')
    msg = utility.base64_decode(msg.encode())
    n = len(msg)

keysizes = []
for k in range(2, min(n // 2, 42)):
    total = 0
    count = 0
    for i in range(0, len(msg), k):
        if i + k + k > len(msg):
            break
        total += utility.hamming_distance(msg[i:i + k].decode(),
                                          msg[i + k:i + k + k].decode())
        count += 1
    keysizes.append((k, total / count / k))

keysizes.sort(key=lambda x: x[1])

max_score = None
answer = None

for i in range(4):
    k = keysizes[i][0]
    lines = [[] for _ in range(k)]
    for j in range(n):
        lines[j % k].append(msg[j])

    bytes_list = []
    valid = True
    for line in lines:
        score, ans = Challenge_4.best_guess(bytes(line))
        if score is None:
            valid = False
            break
        bytes_list.append(ans)

    if not valid:
        continue

    bytes_rearranged = []
    for c in range((n + k - 1) // k):
        for r in range(k):
            if c < len(bytes_list[r]):
                bytes_rearranged.append(bytes_list[r][c])

    score = utility.score_english(bytes(bytes_rearranged))
    if score is not None and (max_score is None or score > max_score):
        answer = bytes(bytes_rearranged).decode()
        max_score = score

assert (max_score is not None), 'answer not found.'
print(answer)
