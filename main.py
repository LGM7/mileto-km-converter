from tkinter import *

window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=250, height=100)
window.config(padx=25, pady=60)
km = 0

input = Entry(width=7)
input.grid(column=1, row=0)
my_label1 = Label(text="Miles", font=("Arial", 10, "bold"))
my_label1.grid(column=2, row=0)

my_label = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label.grid(column=0, row=1)

my_label2 = Label(text=f"{km}", font=("Arial", 10, "bold"))
my_label2.grid(column=1, row=1)

my_label3 = Label(text="Km", font=("Arial", 10, "bold"))
my_label3.grid(column=2, row=1)


def button_clicked():
    new_text = input.get()
    mile = float(new_text)
    km = 1.609 * mile
    my_label.config(text=f"is equal to     {km}     Km", font=("Arial", 10, "bold"))
    my_label.grid(column=0, row=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=0, row=3)

window.mainloop()
