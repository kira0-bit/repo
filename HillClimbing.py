def manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            current_row = i // 3
            current_col = i % 3

            goal_index = goal.index(state[i])
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(blank - 3)

    if row < 2:
        moves.append(blank + 3)

    if col > 0:
        moves.append(blank - 1)

    if col < 2:
        moves.append(blank + 1)

    for move in moves:
        new_state = state.copy()
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        neighbors.append(new_state)

    return neighbors


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def hill_climbing(start, goal):
    current = start
    path = [current]

    while True:
        current_heuristic = manhattan_distance(current, goal)

        if current == goal:
            return path

        neighbors = get_neighbors(current)

        best_neighbor = current
        best_heuristic = current_heuristic

        for neighbor in neighbors:
            h = manhattan_distance(neighbor, goal)

            if h < best_heuristic:
                best_heuristic = h
                best_neighbor = neighbor

        if best_neighbor == current:
            return None

        current = best_neighbor
        path.append(current)


start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

solution = hill_climbing(start, goal)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)
else:
    print("Hill Climbing got stuck at a local optimum.")