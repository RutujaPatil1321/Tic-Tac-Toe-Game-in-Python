from tkinter import *

def callback(r,c):
    global player

#player X's turn
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X',fg='red',bg='white')
        states[r][c] = 'X'
        player = 'O'

#player O's turn
    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O',fg='orange',bg='white')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()

def check_for_winner():
    global stop_game
#checks condition vertically
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].config(bg = 'black')
            b[i][1].config(bg = 'black')
            b[i][2].config(bg = 'black')
            stop_game = True
            
#checks contition horizintally
    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].config(bg = 'black')
            b[1][i].config(bg = 'black')
            b[2][i].config(bg = 'black')
            stop_game = True

#checks condition for upper left corner to lower right corner diagonal
        if states[0][0] == states[1][1] == states[2][2] != 0:
            b[0][0].config(bg = 'black')
            b[1][1].config(bg = 'black')
            b[2][2].config(bg = 'black')
            stop_game = True

#checks condition for upper right corner to lower left corner diagonal
        if states[2][0] == states[1][1] == states[0][2] != 0:
            b[2][0].config(bg = 'black')
            b[1][1].config(bg = 'black')
            b[0][2].config(bg = 'black')
            stop_game = True

#window
root = Tk()
root.title("---TIC TAC TOE---")

#Matrix
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]
states = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("Arial",60),width=4,bg='powder blue',command=lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
        player = 'X'
        stop_game = False

mainloop()
