from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Detect if all the courses can be completed or not provided the prerequisites

            - Time complexity: O(V+E)
            - Space complexity: O(V)

        Args:
            numCourses (int): Input number of courses
            prerequisites (List[List[int]]): Input prerequisites

        Returns:
            bool: True if all the courses can be completed, else False
        """

        # (a,b) means edge (b->a)
        adj = defaultdict(list)
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])

        in_degree = [0] * numCourses
        for edge in prerequisites:
            in_degree[edge[0]] += 1

        queue = deque()
        for vertex in range(numCourses):
            if in_degree[vertex] == 0:
                queue.append(vertex)

        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for neighbour in adj[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if count == numCourses:
            return True

        return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Find the order of courses to be taken to complete all the courses

            - Time complexity: O(V+E)
            - Space complexity: O(V)

        Args:
            numCourses (int): Input number of courses
            prerequisites (List[List[int]]): Input prerequisites

        Returns:
            List[int]: Order of courses to be taken to complete all the courses
        """
        # (a,b) means edge (b->a)
        adj = defaultdict(list)
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])

        in_degree = [0] * numCourses
        for edge in prerequisites:
            in_degree[edge[0]] += 1

        queue = deque()
        for vertex in range(numCourses):
            if in_degree[vertex] == 0:
                queue.append(vertex)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for neighbour in adj[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if len(topo) == numCourses:
            return topo

        return []
