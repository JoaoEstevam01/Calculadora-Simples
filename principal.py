from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#0a0a0a'   #black
cor2 = '#c71a2e'   #vermelho
cor3 = '#fffdd0'   #creme

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

#Botoes

b_1 = Button(frame_body, text='C', width=11, height=2)
b_1.place(x=0, y=0)

janela.mainloop()