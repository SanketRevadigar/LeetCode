import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)
        for n1,n2 in edges:                         #create a hashmap for graph neighbours
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)               #as its undirected add both pairs
        queue,visited = deque(),set()               #queue for bfs and visited to track edges
        queue.append(source)
        visited.add(source)
        while queue:
            node = queue.popleft()
            if node == destination:                 #if current element is dest, return True
                return True
            for adj in neighbours[node]:            #check for its neighbour edges also
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
        return False
            