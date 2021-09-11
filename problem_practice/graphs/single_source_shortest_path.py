#find the shortest path of all the nodes fron the node 0
# but usually this method is not suggested as it used recursion and it might be possible some tree will go so deep that our recursion buffer
# might get full

def dfs(node):
    visited[node] = True
    for i in adj_list[node]:
        if (visited[i] == False):
            distance[i] = min(distance[node] + 1, distance[i])
            dfs(i)
n = int(input())
e = int(input())
adj_list = [[] for i in range(n)]

for j in range(e):
    u, v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

distance = [float("inf")]*n
distance[0] = 0
visited = [False]*n
for i in range(n):
    if (visited[i] == False):
        dfs(i)
print(distance)

