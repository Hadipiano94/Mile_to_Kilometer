import tkinter as tk
import tkinter.ttk


def mile_to_km():
    result.config(text=f"{int(text_box.get()) * 1.6:.1f}")


window = tk.Tk()

frame = tkinter.ttk.Frame(window, padding=20)
frame.grid()

text_box = tk.Entry(frame)
text_box.config(width=7)
text_box.insert(0, string="0")
text_box.grid(column=1, row=0)

result = tk.Label(frame, text="0")
result.grid(column=1, row=1)

text_1 = tk.Label(frame, text="miles")
text_1.grid(column=2, row=0)

text_2 = tk.Label(frame, text="is equal to")
text_2.grid(column=0, row=1)

text_3 = tk.Label(frame, text="km")
text_3.grid(column=2, row=1)

empty_space = tk.Label(frame, text="")
empty_space.grid(column=1, row=2)

key = tk.Button(frame, text="calculate", command=mile_to_km)
key.grid(column=1, row=3)


window.mainloop()
