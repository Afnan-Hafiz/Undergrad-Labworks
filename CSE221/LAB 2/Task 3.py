n = list(map(int, input().split()))
arr = list(map(int, input().split()))
target = n[1]
num = n[0]

found = False

for i in range(num - 2):
    seen = {}
    current_target = target - arr[i]
    for j in range(i + 1, num):
        diff = current_target - arr[j]
        if diff in seen:
            print(i + 1, seen[diff] + 1, j + 1)
            found = True
            break
        seen[arr[j]] = j
    if found:
        break

if not found:
    print("-1")