from tkinter import *


root = Tk()

root['bg'] = '#35676e'
root.title('EXMO&bot v1.0')
#root.wm_attributes('-alpha', 0.9)
root.geometry('800x600')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=800, width=600)
canvas.pack()

frame = Frame(root, bg='#35676e')
# (relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='привет', bg='#35676e', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow')
btn.pack()

root.mainloop()
