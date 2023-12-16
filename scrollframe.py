from customtkinter import *
root  = CTk()
root.geometry("700x300")

frame = CTkScrollableFrame(root,)
frame.pack(pady = 40)

for i in range(40):
    CTkButton(frame, text= " this is a btn").pack(pady = 10)

root.mainloop()