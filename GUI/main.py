from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry("925x500+300+200")



root.configure(bg='#fff')
root.resizable(False,False)

def signin():
   pass


img = PhotoImage(file = 'login.png')
Label(root, image=img, bg='white').place(x=50, y=50)
frame = Frame(root, width=350, height= 350, bg='white')
frame.place(x= 490, y=70)
heading = Label(frame, text='Sign In',fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')
#For USERNAME IN SIGN-IN PAGE
user = Entry(frame, width=25,fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light',11 ))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y='107')

#For PASSWORD IN SIGN-IN PAGE
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name == code.get()
    if name == '':
        user.insert(0, 'Password')

code = Entry(frame, width=25,fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light',11 ))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y='177')

Button(frame, width=39,pady=8, text='Login' ,bg='#57a1f8', border=0).place(x=35, y=204)
label =Label(frame, text="Don't have an account?", fg='black', bg='white',font=('Microsoft YaHei UI Light',9 ) )
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white',cursor='hand2', fg='#57a1f8', command=signin )
sign_up.place(x=215, y=270)

root.mainloop()