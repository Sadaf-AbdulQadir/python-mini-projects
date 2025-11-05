import tkinter as tk
from tkinter import ttk, Text

def perform_operation():
    op = operation.get("1.0","end-1c")
    try:
        output = eval(op)
        res.config(text=f"Result is {output}")
    except:
        res.config(text="Incorrect input. Try again")
root = tk.Tk()
root.title("Evaluator")
root.geometry("500x300")
root.resizable(True,True)

frame = ttk.Frame(root)
frame.pack(pady=5)

tk.Label(frame,text='Expression Evaluator',font=("Arial",16,"bold")).grid(row=0,column=0,padx=15,pady=15)
operation = Text(frame,bg='light gray',height=3,width=20,font=("Arial",14,"bold"))
operation.grid(row=1,column=0)
res = tk.Label(frame,font=("Arial",10,"bold"))
res.grid(row=4,column=0,padx=15,pady=15)
button = ttk.Button(root, text="Solve", command=perform_operation)
button.pack(pady=10)

root.mainloop()
