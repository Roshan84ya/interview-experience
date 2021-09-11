#problem statement https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/
# so whenever we run a dfs is goes like depth first serach and visits all the node which are connected with the starting node
# so the number of disconnected component will be equal to number of time dfs ran
def dfs(node):
    visited[node] = True
    for i in adj_list[node]:
        if (visited[i]==False):
            dfs(i)

n, e = map(int,input().split())
adj_list = [[] for i in range(n+1)]
for i in range(e):
    u, v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

visited = [False]*(n+1)
k = 0
for i in range(1, n+1):
    if (visited[i] == False):
        dfs(i)
        k += 1
print(k)