WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(board):
    for a,b,c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return 'draw' if all(board) else None

def evaluate(board, ai, human):
    result = winner(board)
    if result == ai: return 10
    if result == human: return -10
    if result == 'draw': return 0
    return None

def minimax(board, depth, alpha, beta, maximizing, ai, human, stats):
    stats['nodes'] += 1
    score = evaluate(board, ai, human)
    if score is not None:
        if score == 10: return score - depth
        if score == -10: return score + depth
        return 0
    if maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = ai
                value = minimax(board, depth+1, alpha, beta, False, ai, human, stats)
                board[i] = ''
                best = max(best, value); alpha = max(alpha, best)
                if beta <= alpha:
                    stats['pruned'] += 1
                    break
        return best
    best = float('inf')
    for i in range(9):
        if board[i] == '':
            board[i] = human
            value = minimax(board, depth+1, alpha, beta, True, ai, human, stats)
            board[i] = ''
            best = min(best, value); beta = min(beta, best)
            if beta <= alpha:
                stats['pruned'] += 1
                break
    return best

def find_best_move(board, ai='O', human='X'):
    if winner(board) is not None:
        return {'move': None, 'score': 0, 'nodes': 0, 'pruned': 0, 'saved_percent': 0}
    stats = {'nodes': 0, 'pruned': 0}
    best_score = -float('inf'); best_move = None
    preferred = [4,0,2,6,8,1,3,5,7]
    for i in preferred:
        if board[i] == '':
            board[i] = ai
            score = minimax(board, 0, -float('inf'), float('inf'), False, ai, human, stats)
            board[i] = ''
            if score > best_score:
                best_score, best_move = score, i
    nodes = stats['nodes']; pruned = stats['pruned']
    saved = min(99, round((pruned / max(1, nodes)) * 100))
    return {'move': best_move, 'score': int(best_score), 'nodes': nodes, 'pruned': pruned, 'saved_percent': saved}
