from flask import Flask, render_template, request, jsonify
from ai.minimax import find_best_move

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/api/move')
def ai_move():
    data = request.get_json(silent=True) or {}
    board = data.get('board')
    if not isinstance(board, list) or len(board) != 9:
        return jsonify({'error': 'Board must contain exactly 9 cells.'}), 400
    if any(cell not in ('', 'X', 'O') for cell in board):
        return jsonify({'error': 'Invalid board values.'}), 400
    return jsonify(find_best_move(board, ai='O', human='X'))

if __name__ == '__main__':
    app.run(debug=True)
