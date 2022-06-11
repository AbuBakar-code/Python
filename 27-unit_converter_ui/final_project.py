from tkinter import *

window = Tk()
# window.minsize(width=500, height=300)
window.title("Miles to Killometer Converter")
window.config(padx=50, pady=50)

def miles_to_km():
    miles = float(input_m.get())
    km = miles* 1.609
    input_km.config(text=f"{km}")

input_m = Entry(width=8)
input_m.grid(column=1, row=0)

input_lable = Label(text="Miles")
input_lable.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

input_km= Label(text= 0)
input_km.grid(column=1, row=1)

input_lable_km = Label(text="Km")
input_lable_km.grid(column=2, row=1)

button = Button(text="Calculate", command= miles_to_km)
button.grid(column=1, row=2)


window.mainloop()