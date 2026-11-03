import heapq

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]


class Node:
    def __init__(self, state, x, y, g, parent):
        # Deep copy of the 3x3 board
        self.state = [row[:] for row in state]
        self.x = x          # row of the blank
        self.y = y          # column of the blank
        self.g = g          # cost so far (moves made)
        self.parent = parent

        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        # Number of misplaced tiles (blank not counted)
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0 and self.state[i][j] != GOAL[i][j]:
                    count += 1
        return count

    def is_goal(self):
        return self.state == GOAL

    def get_key(self):
        # String form of the board, used to track visited states
        return "".join(str(self.state[i][j]) for i in range(3) for j in range(3))

    def print_state(self):
        for row in self.state:
            print(*row)
        print()


# Row/column changes for up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def print_path(node):
    if node is None:
        return
    print_path(node.parent)
    node.print_state()


def a_star(start, x, y):
    # Heap entries are (f, counter, node). The counter breaks ties so
    # Python never has to compare two Node objects directly.
    counter = 0
    pq = []
    heapq.heappush(pq, (0, counter, Node(start, x, y, 0, None)))

    visited = set()

    while pq:
        _, _, current = heapq.heappop(pq)

        if current.get_key() in visited:
            continue
        visited.add(current.get_key())

        if current.is_goal():
            print("Goal State Reached!\n")
            print_path(current)
            return

        for k in range(4):
            nx = current.x + dx[k]
            ny = current.y + dy[k]

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in current.state]

                # Swap the blank with the neighboring tile
                new_state[current.x][current.y], new_state[nx][ny] = (
                    new_state[nx][ny],
                    new_state[current.x][current.y],
                )

                child = Node(new_state, nx, ny, current.g + 1, current)

                if child.get_key() not in visited:
                    counter += 1
                    heapq.heappush(pq, (child.f, counter, child))

    print("No Solution Found.")


if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8],
    ]

    x, y = 1, 1  # Position of the blank (0)

    a_star(start, x, y)