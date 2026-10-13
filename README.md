# Tic-Tac-Toe AI — Minimax + Alpha-Beta Pruning

Complete mini-project: modern responsive web GUI + Python Flask backend + Minimax/Alpha-Beta AI.

## Features
- Human (X) vs AI (O)
- Minimax decision-making
- Alpha-Beta pruning
- AI search statistics
- Dark/light mode
- Match history saved in browser localStorage
- Result popup and responsive design

## Run in VS Code (Windows)
1. Install Python 3.10+.
2. Open this folder in VS Code.
3. Terminal: `python -m venv venv`
4. Activate: `venv\Scripts\activate`
5. Install: `pip install -r requirements.txt`
6. Start: `python app.py`
7. Open: `http://127.0.0.1:5000`

## Project Structure
```text
Tic_Tac_Toe_AI_Minimax_AlphaBeta/
├── app.py
├── requirements.txt
├── README.md
├── run_windows.bat
├── ai/
│   ├── __init__.py
│   └── minimax.py
├── templates/index.html
└── static/
    ├── css/style.css
    └── js/app.js
```

## AI Logic
- AI = O, Human = X
- AI win = +10
- Draw = 0
- Human win = -10
- Minimax searches future game states.
- Alpha-Beta pruning skips branches that cannot affect the final decision.
- Move ordering checks the center and corners early to improve pruning.

## Technologies
Python, Flask, HTML5, CSS3, JavaScript, Minimax, Alpha-Beta Pruning.
