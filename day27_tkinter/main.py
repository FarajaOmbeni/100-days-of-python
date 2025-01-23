from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

answer = Label(text="0")
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

def convert_to_km():
    miles_entry = float(entry.get())
    miles_entry *= 1.609344
    answer.config(text=f"{round(miles_entry)}")

button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()