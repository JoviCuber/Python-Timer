from tkinter import *
import winsound
class App:
    def __init__(self,tex):
        self.text = tex
    def update(self):
        self.text.config(text=str(self.tim//3600)+":"+str(self.tim//60)+":"+str(self.tim%60))
        if self.tim != 0:
            self.tim = self.tim - 1
            self.text.after(1000,self.update)
        else:
            winsound.PlaySound('windows_10_alarm_1.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
            btn2.config(state='normal')
    def timer_function(self):
        self.tim = int(timer.get())
        if timer.get() == 0 or timer.get == '':
            canvas.itemconfig(d, state='normal')
        else:
            btn1.config(state='disabled')
            canvas.itemconfig(d, state='hidden')
            self.text.config(text=str(self.tim))
            self.update()
    def dismiss(self):
        btn1.config(state='normal')
        btn2.config(state='disabled')
        winsound.PlaySound(None, 0)
tk = Tk()
tk.title("Timer")
tk.resizable(0,0)
tk.iconbitmap('Logo.ico')
timer = IntVar()
canvas = Canvas(tk, width=200, height=200, bg='#0080FF')
canvas.pack()
text = Label(tk, text='0', font=("Impact", 20,),bg='#0080FF',fg='white')
hint = canvas.create_text(100,160, text="Write value in seconds", font=("", 10),fill='white')
app = App(text)
play = PhotoImage(file='play.gif')
d = canvas.create_text(102, 72, text="You didn't write a normal value!", font=("", 10), fill='white', state='hidden')
box = Entry(font=("", 12), textvariable=timer)
btn1 = Button(tk, command=app.timer_function, text='', width=40, height=42, border=0,image=play,activebackground='#0080FF',bg="#0080FF")
btn2 = Button(tk, command=app.dismiss, text='Dismiss', width=8, height=2,state='disabled',border=0,activebackground='#c9c9c9')
canvas.create_window(100,180,window=box)
canvas.create_window(50,40,window=btn1)
canvas.create_window(155,40, window=btn2)
canvas.create_window(100,100,window=text)
tk.mainloop()
