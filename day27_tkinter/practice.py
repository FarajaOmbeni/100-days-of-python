from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
label.config(padx=20, pady=20)

label['text'] = "New Text"

#Button
def button_clicked():
    label['text'] = my_input.get()

button = Button(text="Submit", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


#Entry
my_input = Entry(width=30)
my_input.insert(END, string='Placeholder')
my_input.grid(column=3, row=2)

window.mainloop()