def minimax(node, depth, maximizing_player):

    if depth == 0:
        return node

    if maximizing_player:
        best_value = float('-inf')

        for child in node:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)

        return best_value

    else:
        best_value = float('inf')

        for child in node:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)

        return best_value

game_tree = [
    [
        [
            [3, 5],
            [2, 9]
        ],
        [
            [1, 4],
            [6, 8]
        ]
    ],
    [
        [
            [7, 2],
            [0, 5]
        ],
        [
            [4, 1],
            [8, 3]
        ]
    ]
]

result = minimax(game_tree, 4, True)

print("Best value:", result)