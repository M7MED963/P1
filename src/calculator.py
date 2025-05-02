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
    except Exception:
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
root.configure(bg="#1e1e1e")

entry = tk.Entry(root, font="Arial 24", bg="#252526", fg="white", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

buttons_frame = tk.Frame(root, bg="#1e1e1e")
buttons_frame.pack()

buttons = [
    ['(', ')', 'C', 'CE', '√'],
    ['π', 'e^', 'e', '^', '/'],
    ['7', '8', '9', '*', 'log'],
    ['4', '5', '6', '-', 'ln'],
    ['1', '2', '3', '+', '='],
    ['0', '.', ]
]

color_map = {
    'C': '#003f5c', 'CE': '#003f5c', '(': '#58508d', ')': '#58508d',
    '√': '#bc5090', '^': '#bc5090', 'log': '#bc5090', 'ln': '#bc5090',
    '+': '#ff6361', '-': '#ff6361', '*': '#ff6361', '/': '#ff6361', '=': '#ffa600',
    'π': '#7a5195', 'e^': '#7a5195', 'e': '#7a5195',
    '0': '#2f4b7c', '1': '#2f4b7c', '2': '#2f4b7c', '3': '#2f4b7c',
    '4': '#2f4b7c', '5': '#2f4b7c', '6': '#2f4b7c', '7': '#2f4b7c',
    '8': '#2f4b7c', '9': '#2f4b7c', '.': '#2f4b7c'
}

for row in buttons:
    row_frame = tk.Frame(buttons_frame, bg="#1e1e1e")
    row_frame.pack(fill=tk.BOTH, expand=True)
    for btn_text in row:
        btn_color = color_map.get(btn_text, "#3e3e3e")
        btn = tk.Button(
            row_frame, text=btn_text, font="Arial 18 bold", height=2, width=5,
            bg=btn_color, fg="white", bd=1, relief=tk.RAISED, activebackground="#444"
        )
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
