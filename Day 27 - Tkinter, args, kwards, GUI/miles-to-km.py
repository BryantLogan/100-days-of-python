from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=60,pady=50)


#   Label
miles_label = Label(text="miles")
miles_label.grid(column=2,row=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=2)

km = Label(text="Km")
km.grid(column=2, row=2)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=2)


#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=3)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1,row=1)






window.mainloop()