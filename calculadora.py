from tkinter import *
from tkinter import ttk

#Cores
cor1 = '#0a0a0a'   #black
cor2 = '#ffab40'   #laranja
cor3 = '#8c8c8c'   #cinza
cor4 = '#3c3e3e'   #tom de cinza
cor5 = '#fafcfb'   #branco

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width=240, height=58, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=240, height=268)
frame_body.grid(row=1, column=0)

#Label
app_label = Label(frame_tela, text='123456789', width=16, height=2, padx=7, relief='flat', anchor='e', justify='right', font=('SFPro 18'), fg=cor5, bg=cor1)
app_label.place(x=0, y=10)

#Botoes
b_1 = Button(frame_body, text='C', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_1.place(x=0, y=0)
b_2 = Button(frame_body, text='+/-', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_2.place(x=60, y=0)
b_3 = Button(frame_body, text='%', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_3.place(x=120, y=0)
b_4 = Button(frame_body, text='/', width=5, height=2, bg=cor2, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_4.place(x=180, y=0)

b_5 = Button(frame_body, text='7', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_5.place(x=0, y=52)
b_6 = Button(frame_body, text='8', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_6.place(x=60, y=52)
b_7 = Button(frame_body, text='9', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_7.place(x=120, y=52)
b_8 = Button(frame_body, text='x', width=5, height=2, bg=cor2, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_8.place(x=180, y=52)

b_9 = Button(frame_body, text='4', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_9.place(x=0, y=104)
b_10 = Button(frame_body, text='5', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_10.place(x=60, y=104)
b_11 = Button(frame_body, text='6', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_11.place(x=120, y=104)
b_12 = Button(frame_body, text='-', width=5, height=2, bg=cor2, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_12.place(x=180, y=104)

b_13 = Button(frame_body, text='1', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_13.place(x=0, y=156)
b_14 = Button(frame_body, text='2', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_14.place(x=60, y=156)
b_15 = Button(frame_body, text='3', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_15.place(x=120, y=156)
b_16 = Button(frame_body, text='+', width=5, height=2, bg=cor2, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_16.place(x=180, y=156)

b_17 = Button(frame_body, text='0', width=12, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_17.place(x=0, y=208)
b_18 = Button(frame_body, text=',', width=5, height=2, bg=cor3, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_18.place(x=120, y=208)
b_19 = Button(frame_body, text='=', width=5, height=2, bg=cor2, font=('SFPro 13 bold'), relief='raised', overrelief='ridge')
b_19.place(x=180, y=208)


janela.mainloop()