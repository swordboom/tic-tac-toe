import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

board = ['' for _ in range(9)]
current_player = 'X'
vs_computer = False
buttons = []

x_img = ctk.CTkImage(Image.open("assets/glow_x.png"), size=(80, 80))
o_img = ctk.CTkImage(Image.open("assets/glow_o.png"), size=(80, 80))

def check_winner(brd):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if brd[cond[0]] == brd[cond[1]] == brd[cond[2]] != '':
            return brd[cond[0]]
    if '' not in brd:
        return 'Draw'
    return None

def reset_board():
    global board, current_player
    board = ['' for _ in range(9)]
    current_player = 'X'
    for btn in buttons:
        btn.configure(image=None, text='', state='normal')

def button_click(index):
    global current_player
    if board[index] == '' and not check_winner(board):
        board[index] = current_player
        if current_player == 'X':
            buttons[index].configure(image=x_img, text='')
        else:
            buttons[index].configure(image=o_img, text='')
        buttons[index].configure(state='disabled')

        winner = check_winner(board)
        if winner:
            show_result(winner)
            return

        if vs_computer and current_player == 'X':
            current_player = 'O'
            ai_move()
        else:
            current_player = 'X' if current_player == 'O' else 'O'

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    if move is not None:
        board[move] = 'O'
        buttons[move].configure(image=o_img, text='', state='disabled')
    winner = check_winner(board)
    if winner:
        show_result(winner)
    else:
        global current_player
        current_player = 'X'

def minimax(brd, is_max):
    result = check_winner(brd)
    if result == 'X':
        return -1
    elif result == 'O':
        return 1
    elif result == 'Draw':
        return 0
    if is_max:
        best_score = -float('inf')
        for i in range(9):
            if brd[i] == '':
                brd[i] = 'O'
                score = minimax(brd, False)
                brd[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if brd[i] == '':
                brd[i] = 'X'
                score = minimax(brd, True)
                brd[i] = ''
                best_score = min(score, best_score)
        return best_score

def show_result(winner):
    msg = f"{winner} wins!" if winner != 'Draw' else "It's a draw!"
    messagebox.showinfo("Game Over", msg)
    reset_board()

def start_game(mode):
    global vs_computer
    vs_computer = mode
    reset_board()

app = ctk.CTk()
app.title("Tic Tac Toe - CustomTkinter")
app.geometry("400x520")
app.resizable(False, False)

main_frame = ctk.CTkFrame(app)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

title = ctk.CTkLabel(main_frame, text="Tic Tac Toe", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=10)

frame = ctk.CTkFrame(main_frame)
frame.pack(pady=10)
frame.grid_columnconfigure((0, 1, 2), weight=1)
frame.grid_rowconfigure((0, 1, 2), weight=1)

for i in range(9):
    btn = ctk.CTkButton(
        frame, text='', width=80, height=80, font=ctk.CTkFont(size=20),
        corner_radius=10, command=lambda i=i: button_click(i),
        fg_color="transparent", hover_color="#4444ff"
    )
    btn.grid(row=i//3, column=i%3, padx=8, pady=8, sticky='nsew')
    buttons.append(btn)

control_frame = ctk.CTkFrame(main_frame)
control_frame.pack(pady=10)

pvp_btn = ctk.CTkButton(control_frame, text="2 Player Mode", width=120, command=lambda: start_game(False))
pvc_btn = ctk.CTkButton(control_frame, text="Vs Computer", width=120, command=lambda: start_game(True))
exit_btn = ctk.CTkButton(control_frame, text="Exit", width=120, command=app.destroy)

pvp_btn.grid(row=0, column=0, padx=5)
pvc_btn.grid(row=0, column=1, padx=5)
exit_btn.grid(row=0, column=2, padx=5)

app.mainloop()
