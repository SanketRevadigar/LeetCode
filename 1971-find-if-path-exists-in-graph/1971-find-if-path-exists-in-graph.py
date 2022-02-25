import collections
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours=defaultdict(list)
        for n1,n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
        queue,visited=deque(),set()
        queue.append(source)
        visited.add(source)
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for adj in neighbours[node]:
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
        return False
            