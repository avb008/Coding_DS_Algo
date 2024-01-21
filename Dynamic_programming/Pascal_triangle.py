from sys import *
from collections import *
from math import *
from typing import *


def kthRow(k: int) -> List[int]:
    """Returns the kth row of Pascal's triangle.

        - Time complexity: O(k^2)
        - Space complexity: O(k^2)

    Args:
        k (int): Index of the row to be returned.

    Returns:
        List[int]: The kth row of Pascal's triangle.
    """
    # Write your code here.
    pascal = [[1 for i in range(j + 1)] for j in range(k)]

    for i in range(k):
        for j in range(i):
            if (i - 1) >= 0 and (j - 1) >= 0:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal[k - 1]


def kthRow_v2(k: int) -> List[int]:
    """Returns the kth row of Pascal's triangle.

        - Time complexity: O(k^2)
        - Space complexity: O(k)

    Args:
        k (int): Index of the row to be returned.

    Returns:
        List[int]: The kth row of Pascal's triangle.
    """
    # Write your code here.
    previous = [1]
    for i in range(k):
        current = [1 for j in range(i + 1)]
        for j in range(1, i):
            if (j - 1) >= 0:
                current[j] = previous[j - 1] + previous[j]
        previous = current.copy()

    return current


# C(n,r) = n! / (r! * (n-r)!) , C(n, r-1) = n! / ((r-1)! * (n-r+1)!)
# C(n, r) = C(n, r-1) * (n-r+1) / r , c(n, 0) = 1
def kthRowOptimized(k: int) -> List[int]:
    """Returns the kth row of Pascal's triangle.

        - Time complexity: O(k)
        - Space complexity: O(k)

    Args:
        k (int): Index of the row to be returned.

    Returns:
        List[int]: The kth row of Pascal's triangle.
    """
    row = [1]
    for i in range(1, k):
        row.append(int(row[i - 1] * (k - i) / i))
    return row


if __name__ == "__main__":
    k = int(stdin.readline().strip())
    print(kthRow(k))
    print(kthRow_v2(k))
    print(kthRowOptimized(k))
