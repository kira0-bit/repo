from collections import deque


# Generate all possible next states
def get_next_states(a, b, capA, capB):

    states = []

    # Fill Jug A
    states.append((capA, b))

    # Fill Jug B
    states.append((a, capB))

    # Empty Jug A
    states.append((0, b))

    # Empty Jug B
    states.append((a, 0))

    # Pour A -> B
    transfer = min(a, capB - b)
    states.append((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, capA - a)
    states.append((a + transfer, b - transfer))

    return states


# Breadth First Search
def bfs(capA, capB, target):

    start = (0, 0)

    queue = deque()
    queue.append((start, [start]))

    visited = set()

    while queue:

        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            return path

        for state in get_next_states(a, b, capA, capB):

            if state not in visited:
                queue.append((state, path + [state]))

    return None


# Depth First Search
def dfs(capA, capB, target):

    start = (0, 0)

    stack = [(start, [start])]

    visited = set()

    while stack:

        (a, b), path = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        if a == target or b == target:
            return path

        next_states = get_next_states(a, b, capA, capB)

        # Reverse to maintain a natural exploration order
        for state in reversed(next_states):

            if state not in visited:
                stack.append((state, path + [state]))

    return None


# ---------------- MAIN PROGRAM ----------------

capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

print("\nChoose Search Algorithm")
print("1. BFS")
print("2. DFS")

choice = int(input("Enter choice: "))

if choice == 1:
    solution = bfs(capA, capB, target)
    algorithm = "BFS"

elif choice == 2:
    solution = dfs(capA, capB, target)
    algorithm = "DFS"

else:
    print("Invalid Choice")
    exit()


if solution:
    print("\nSolution using", algorithm)
    print("-------------------------")

    for state in solution:
        print(state)

else:
    print("\nNo Solution Found.")