import tkinter as tk
import math

def evaluate_expression(expression):
    expression = expression.replace("^", "**")
    expression = expression.replace("√", "math.sqrt")
    expression = expression.replace("log", "math.log10")
    expression = expression.replace("ln", "math.log")
    expression = expression.replace("e^", "math.exp")
    expression = expression.replace("π", str(math.pi))
    expression = expression.replace("e", str(math.e))
    
    try:
        return str(eval(expression))
    except:
        return "Error"

def click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        result = evaluate_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ['7', '8', '9', '/', '√'],
    ['4', '5', '6', '*', '^'],
    ['1', '2', '3', '-', 'log'],
    ['0', '.', '=', '+', 'ln'],
    ['π', 'e^', 'e', 'C']
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(fill=tk.BOTH)
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", click)

root.mainloop()
