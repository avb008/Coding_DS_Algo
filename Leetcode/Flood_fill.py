from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """Flood fill algorithm.

        Args:
            image (List[List[int]]): Image to be modified.
            sr (int): Target row.
            sc (int): Target column.
            color (int): Color to be filled.

        Returns:
            List[List[int]]: Modified image.
        """
        rows = len(image)
        cols = len(image[0])
        r_d = [-1, 0, 1, 0]
        c_d = [0, 1, 0, -1]

        modified_image = image.copy()
        queue = deque([(sr, sc)])
        target = image[sr][sc]

        while queue:
            x, y = queue.popleft()
            modified_image[x][y] = color

            for i in range(4):
                x_r, y_r = x + r_d[i], y + c_d[i]
                if 0 <= x_r < rows and 0 <= y_r < cols:
                    if modified_image[x_r][y_r] != 0 and image[x_r][y_r] == target:
                        queue.append((x_r, y_r))

        return modified_image
