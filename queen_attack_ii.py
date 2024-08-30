"""
You will given a square chess board with one queen and a number of obstacles placed on it.
Determine how many squares the queen can attack.

A queen is standing on an n x n chessboard.
The chess board's rows are numbered from 1 to n, going from bottom to top.
Its columns are numbered from 1 to n, going from left to right.
Each square is refernced by a tuple, (r, c), describing the row, r, and column, c,
where the square is located.

The queen is standing at position (rq, cq). In a single move,
she can attack any square in any of the eight
directions (left, right, up, down, and the four diagonals).

There are obstacles on the chessboard, each preventing the queen from attacking any square
beyond it on that path.

For example, queen on (4, 4), an obstacle at location (3, 5) prevents the queen from
attacking cells (3, 5), (2, 6), and (1, 7). Thus there are 24 squares the queen can attack
from here position.

Given the queen's position and the locations of all the obstacles, find and print
the number of squares the queen can attack from her position at (rq, cq).
"""

# NOTE:
# - Moving to the 8 directions of the board implemented by vectors "directions"
# - Using 'List' for 'obstacles' is not efficient. Change the type to a 'Set' is crutial..
## - to make it pass tests considering time efficiency. The changing is made from withing the function itself.
# - Also, for the vairable of moving 'next_square', 'Tuple' type is used, as it's too more efficient.
# - The conditional check for 'next_square' in the 'wile loop' optimized too.


import os


def queen_attack(n, k, r_q, c_q, obstacles):
    """
    Parameters:
        int n: the number of rows and columns in the board.
        int k: the number of obstacles on the obard.
        int r_q: the row number of the queen's position.
        int c_q: the column number of the queen's position.
        int obstacles[k][2]: each element is an array of 2 integers,
            the row and column of an obstacle.

    Returns:
        int: the number of squares the queen can attack.

    Input Format:
        The first line contains two space-separated integers n and k,
        the length of the board's sides and the number of obstacles.
        The next line contains two space-separated integers rq and cq,
        the queen's row and column position.

        Each of the next k lines contains two space-separated integers r[i] and c[i],
        the row and column position of obstacle[i]

    Constraints
        0 < n <= 10^5
        0 <= k <= 10^5

        A single cell may contain more than one obstacle.
        There will never be an obstacle at the position where the queen is located.

    """

    obstacles = set(tuple(obstacle) for obstacle in obstacles)

    directions = [
        [1, 0],  # UP
        [-1, 0],  # DOWN
        [0, -1],  # LEFT
        [0, 1],  # RIGHT
        [1, -1],  # UP LEFT
        [1, 1],  # UP RIGHT
        [-1, -1],  # DOWN LEFT
        [-1, 1],  # DOWN RIGHT
    ]
    number_of_squares_queen_can_attack = 0

    for direction in directions:
        # get the next square location for given directon
        next_square = (r_q + direction[0], c_q + direction[1])

        while (
            1 <= next_square[0] <= n
            and 1 <= next_square[1] <= n
            and next_square not in obstacles
        ):

            number_of_squares_queen_can_attack += 1

            # continue to the next square in the same direction
            next_square = (next_square[0] + direction[0], next_square[1] + direction[1])

    return number_of_squares_queen_can_attack


if __name__ == "__main__":

    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queen_attack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + "\n")

    fptr.close()
