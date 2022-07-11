from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random


#------------------Colors----------------#
BLUE = "#4F98CA"
WHITE = "#EFFFFB"
BLACK = "#272727"
GREEN = "#50D890"

#------------------Screen----------------#
window = Tk()
window.title("Tic Tac Toe")
window.wm_iconbitmap('ICO.ico')
window.resizable(width=False, height=False)
window.geometry('506x581')

#------------------Images----------------#
# Read the Image
xphoto = Image.open("x.png")
ophoto = Image.open("o.png")
# Resize the image using resize() method
xphoto = xphoto.resize((100, 100))
ophoto = ophoto.resize((100, 100))

xphoto = ImageTk.PhotoImage(xphoto)
ophoto = ImageTk.PhotoImage(ophoto)

#------------------Logic----------------#

clicked = True
count = 0

def b_click(b,num,r,c):
    global clicked, count

    if clicked == True:
        labelPhoto = Label(image=xphoto,height=150,width=150,highlightthickness=0,background=BLACK)
        labelPhoto.grid(row=r,column=c)
        if num == 1:
            button_1['text'] = 'X'
        elif num == 2:
            button_2['text'] = 'X'
        elif num == 3:
            button_3['text'] = 'X'
        elif num == 4:
            button_4['text'] = 'X'
        elif num == 5:
            button_5['text'] = 'X'
        elif num == 6:
            button_6['text'] = 'X'
        elif num == 7:
            button_7['text'] = 'X'
        elif num == 8:
            button_8['text'] = 'X'
        elif num == 9:
            button_9['text'] = 'X'

        clicked = False
        count += 1
        who_wins()

    else:
        labelPhoto = Label(image=ophoto,height=150,width=150,highlightthickness=0,background=BLACK)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            button_1['text'] = 'O'
        elif num == 2:
            button_2['text'] = 'O'
        elif num == 3:
            button_3['text'] = 'O'
        elif num == 4:
            button_4['text'] = 'O'
        elif num == 5:
            button_5['text'] = 'O'
        elif num == 6:
            button_6['text'] = 'O'
        elif num == 7:
            button_7['text'] = 'O'
        elif num == 8:
            button_8['text'] = 'O'
        elif num == 9:
            button_9['text'] = 'O'
        clicked = True
        count += 1
        who_wins()

def randomstarter():
    random_starter = random.randint(0,1)
    if random_starter == 0:
        click = True
    else:
        click = False
    return click

def who_wins():
    global count,player_x,player_o, clicked

    if button_1['text'] == 'X' and button_2['text'] == 'X' and button_3['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe","Player X Wins!")
        clicked = randomstarter()
        count = 0
        player_x += 1
        canvas = Canvas()
        canvas.create_line(300, 35, 300, 200, width=5)
        canvas.grid(row=1,colum=0,rowspan=3)
        clear()

    elif button_4['text'] == 'X' and button_5['text'] == 'X' and button_6['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        count = 0
        player_x += 1
        clear()

    elif button_7['text'] == 'X' and button_8['text'] == 'X' and button_9['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        count = 0
        player_x += 1
        clear()

    elif button_1['text'] == 'X' and button_4['text'] == 'X' and button_7['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        count = 0
        player_x += 1
        clear()

    elif button_2['text'] == 'X' and button_5['text'] == 'X' and button_8['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        count = 0
        player_x += 1
        clear()

    elif button_3['text'] == 'X' and button_6['text'] == 'X' and button_9['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        player_x += 1
        count = 0
        clear()

    elif button_1['text'] == 'X' and button_5['text'] == 'X' and button_9['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe", "Player X Wins!")
        clicked = randomstarter()
        player_x += 1
        count = 0
        clear()
    elif button_3['text'] == 'X' and button_5['text'] == 'X' and button_7['text'] == 'X':
        messagebox.showinfo("Tic Tac Toe","Player X Wins!")
        clicked = randomstarter()
        player_x += 1
        count = 0
        clear()

    elif button_1['text'] == 'O' and button_2['text'] == 'O' and button_3['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_4['text'] == 'O' and button_5['text'] == 'O' and button_6['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_7['text'] == 'O' and button_8['text'] == 'O' and button_9['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_1['text'] == 'O' and button_4['text'] == 'O' and button_7['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_2['text'] == 'O' and button_5['text'] == 'O' and button_8['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_3['text'] == 'O' and button_6['text'] == 'O' and button_9['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_1['text'] == 'O' and button_5['text'] == 'O' and button_9['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif button_3['text'] == 'O' and button_5['text'] == 'O' and button_7['text'] == 'O':
        messagebox.showinfo("Tic Tac Toe","Player O Wins!")
        clicked = randomstarter()
        player_o += 1
        count = 0
        clear()

    elif count == 9:
        messagebox.showinfo("Tic Tac Toe", "Tie Game!")
        clicked = randomstarter()
        count = 0
        clear()


def clear():
    global button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9, clicked

    if clicked == True:
        messagebox.showinfo("Starting Player","X Starts!")
    else:
        messagebox.showinfo("Starting Player","Player O Starts!")
    button_1 = Button(text="")
    button_1.grid(row=1, column=0)
    button_1.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_1, 1, 1, 0))

    button_2 = Button(text="")
    button_2.grid(row=1, column=1)
    button_2.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_2, 2, 1, 1))

    button_3 = Button(text="")
    button_3.grid(row=1, column=2)
    button_3.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_3, 3, 1, 2))

    button_4 = Button(text="")
    button_4.grid(row=2, column=0)
    button_4.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_4, 4, 2, 0))

    button_5 = Button(text="")
    button_5.grid(row=2, column=1)
    button_5.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_5, 5, 2, 1))

    button_6 = Button(text="")
    button_6.grid(row=2, column=2)
    button_6.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_6, 6, 2, 2))

    button_7 = Button(text="")
    button_7.grid(row=3, column=0)
    button_7.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_7, 7, 3, 0))

    button_8 = Button(text="")
    button_8.grid(row=3, column=1)
    button_8.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                    command=lambda: b_click(button_8, 8, 3, 1))

    button_9 = Button(text="")
    button_9.grid(row=3, column=2)
    button_9.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, fg=BLACK, borderwidth=.5,
                    background=BLACK, command=lambda: b_click(button_9, 9, 3, 2))

    window.configure(background=BLACK)
    x_score = Label(text=f"X Score : {player_x}", fg=GREEN, bg=BLACK, highlightthickness=0, height=2,
                    font=("Futura", 18, "bold"))
    x_score.grid(row=0, column=0)

    o_score = Label(text=f"O Score : {player_o}", fg=WHITE, bg=BLACK, highlightthickness=0, height=2,
                    font=("Futura", 18, "bold"))
    o_score.grid(row=0, column=2)


player_x = 0
player_o = 0

#------------------Labels----------------#
window.configure(background=BLACK)
x_score = Label(text=f"X Score : {player_x}",fg=GREEN,bg=BLACK, highlightthickness=0,height=2, font=("Futura", 18,"bold"))
x_score.grid(row=0,column=0)

o_score = Label(text=f"O Score : {player_o}",fg=WHITE,bg=BLACK, highlightthickness=0,height=2, font=("Futura", 18, "bold"))
o_score.grid(row=0,column=2)

#------------------Buttons----------------#

WIDTH = 23
HEIGHT = 11

button_1 = Button(text="")
button_1.grid(row=1, column=0)
button_1.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_1, 1, 1, 0))

button_2 = Button(text="")
button_2.grid(row=1, column=1)
button_2.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_2, 2, 1, 1))

button_3 = Button(text="")
button_3.grid(row=1, column=2)
button_3.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_3, 3, 1, 2))

button_4 = Button(text="")
button_4.grid(row=2, column=0)
button_4.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_4, 4, 2, 0))

button_5 = Button(text="")
button_5.grid(row=2, column=1)
button_5.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_5, 5, 2, 1))

button_6 = Button(text="")
button_6.grid(row=2, column=2)
button_6.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_6, 6, 2, 2))

button_7 = Button(text="")
button_7.grid(row=3, column=0)
button_7.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_7, 7, 3, 0))

button_8 = Button(text="")
button_8.grid(row=3, column=1)
button_8.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, borderwidth=.5, background=BLACK,
                command=lambda: b_click(button_8, 8, 3, 1))

button_9 = Button(text="")
button_9.grid(row=3, column=2)
button_9.config(width=WIDTH, height=HEIGHT, relief=SUNKEN, activebackground=BLACK, fg=BLACK, borderwidth=.5,
                background=BLACK, command=lambda: b_click(button_9, 9, 3, 2))




window.mainloop()

