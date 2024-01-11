from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Find the number of provinces

            - Time Complexity: O(V + E)
            - Space Complexity: O(V)

        Args:
            isConnected (List[List[int]]): Adjacency matrix

        Returns:
            int: Number of provinces
        """
        n = len(isConnected)
        visited = [False] * (n + 1)
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1

                queue = deque([i])
                while queue:
                    node = queue.popleft()
                    for i in range(n):
                        if isConnected[node][i] == 1 and visited[i] is False:
                            queue.append(i)
                            visited[i] = True

        return provinces
