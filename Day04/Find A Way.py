import sys
from collections import deque

def solve():
    # Using fast I/O for 40,000 nodes
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n <= 1:
        print(0)
        return

    # 1. Build an adjacency list (treating the tree as an undirected graph)
    adj = [[] for _ in range(n + 1)]
    ptr = 1
    for i in range(1, n + 1):
        l = int(input_data[ptr])
        r = int(input_data[ptr + 1])
        ptr += 2
        
        if l != -1:
            adj[i].append(l)
            adj[l].append(i)
        if r != -1:
            adj[i].append(r)
            adj[r].append(i)

    def bfs(start_node):
        # Returns (farthest_node, distance)
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        
        farthest_node = start_node
        max_dist = 0
        
        while queue:
            u = queue.popleft()
            if distances[u] > max_dist:
                max_dist = distances[u]
                farthest_node = u
            
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
                    
        return farthest_node, max_dist

    # 2. First BFS to find one end of the diameter
    u, _ = bfs(1)
    
    # 3. Second BFS from 'u' to find the other end
    _, diameter = bfs(u)
    
    print(diameter)

if __name__ == "__main__":
    solve()
