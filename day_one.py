import heapq

# Read the file
with open("your_file.txt", "r") as file:
    a, b = [], []
    for line in file:
        left, right = map(int, line.split())
        a.append(left)
        b.append(right)

# Convert lists to heaps
heapq.heapify(a)
heapq.heapify(b)

def solve(a, b):
    res = 0
    while a and b:
        a_curr, b_curr = heapq.heappop(a), heapq.heappop(b)
        res += abs(a_curr - b_curr)
    return res

print(solve(a, b))
