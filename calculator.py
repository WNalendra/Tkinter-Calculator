import tkinter as tk

window = tk.Tk()
window.title("Calculater")
window.geometry("300x300")
window.resizable(False, False)

def entrypressed():
  calculate = eval(entry.get("1.0", tk.END)) 
  labeloutput.configure(text=f"output:{calculate}")
def clearpressed():
  entry.delete("1.0", tk.END)  # Delete text from start to end
  labeloutput.configure(text="Output: ")


inputlabel = tk.Label(text="input:")
inputlabel.pack()
entry = tk.Text(window, width=30, height=2)  # Adjust height here
entry.pack()

entrybutton = tk.Button(window, text="Enter",command=entrypressed)
entrybutton.place(x=90, y=60)
clearbutton = tk.Button(text="Clear", command=clearpressed)
clearbutton.place(x=160, y=60)
labeloutput = tk.Label(text="output")
labeloutput.pack(pady=40)

tk.mainloop()
