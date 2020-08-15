import random
import string
from random import randint
import tkinter as tk
from tkinter import Entry,Label,Button,PhotoImage


prog=tk.Tk()
prog.geometry("600x400")
prog.configure(bg="blue")
prog.title("Random Password Generator(RPG)")
prog.iconphoto(False,PhotoImage(file='lock.png'))

l=Label(text="Number of characters:")
l.configure(bg="blue",fg="white",font=('Comic Sans Ms',10))  #font=('Comic Sans MS',30)
l.place(x=240,y=25)

e=Entry(prog)
e.configure(bg="green")
e.place(x=250,y=50)

def password_generator():
  length=e.get()
  e.delete(0,"end")
  l=int(length)
  if l <10:
    l=10

  num=""
  l_numbers=randint(1,int(l/3))
  for i in range(0,l_numbers):
      num+=str(randint(0,9))
  
  symbols_keyboard="~`!@#$%^&*()_-+={[}]:;|<>,.?\/'"
  sym=""
  l_symbols=randint(1,l_numbers)
  for i in range(0,l_symbols):
      sym+=symbols_keyboard[randint(0,len(symbols_keyboard)-1)]

  all_letters=string.ascii_letters
  lett=""
  l=l-(l_numbers+l_symbols)
  for i in range(0,l):
      lett+=all_letters[randint(0,len(all_letters)-1)]

  password=lett+sym+num

  l=Label(text=f"Your Password:")
  l.configure(bg="blue",fg="white",font=('Comic Sans Ms',10))
  l.place(x=255,y=125)

  k=Entry(prog,text=f"{password}")
  k.insert(0,f"{password}")
  k.configure(bg="yellow")
  k.place(x=250, y=150) 
 



b=Button(text="Generate",command=password_generator)
b.configure(bg="red",fg="white",font=('Comic Sans Ms',10))
b.place(x=280,y=75)
prog.mainloop()




