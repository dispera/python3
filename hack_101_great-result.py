n, k = map(int, input().split())
q = [list(map(int, input().split())) for i in range(n)]
q.sort(key=lambda x: x[1] + x[0], reverse=True)
print(max(0, sum(x[0] for x in q[:k]) - sum(x[1] for x in q[k:])))
