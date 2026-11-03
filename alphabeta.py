def alpha_beta(node, depth, maximizing_player, alpha, beta): 
 
    if depth == 0: 
        return node 
 
    if maximizing_player: 
        best_value = float('-inf') 
 
        for child in node: 
            value = alpha_beta(child, depth - 1, False, alpha, beta) 
            best_value = max(best_value, value) 
 
            alpha = max(alpha, best_value) 
 
            if alpha >= beta: 
                break 
 
        return best_value 
 
    else: 
        best_value = float('inf') 
 
        for child in node: 
 
            value = alpha_beta(child, depth - 1, True, alpha, beta) 
            best_value = min(best_value, value) 
 
            beta = min(beta, best_value) 
 
            if alpha >= beta: 
                break 
 
        return best_value 
 
game_tree = [ 
    [ 
        [-1, 4], 
        [2, 6] 
    ], 
    [ 
        [-3, -5], 
        [0, 7] 
    ] 
] 
 
result = alpha_beta( 
    game_tree, 
    3, 
    True, 
    float('-inf'), 
    float('inf') 
) 
 
print("Best value:", result)