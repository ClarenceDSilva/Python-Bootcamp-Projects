from tkinter import *

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(width=400, height=150)
window.config(padx=120, pady=20)

# Entry
input = Entry(width=15)
# print(input.get())
input.grid(row=1, column=3)
input.insert(END, string="0")

# Labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=5, row=1)
miles_label.config(padx=20, pady=5)

equals_label = Label(text="is equal to", font=("Arial", 10))
equals_label.grid(column=1, row=7)
equals_label.config(padx=10, pady=20)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=5, row=7)
km_label.config(padx=10, pady=20)

ans_label = Label(text="0", font=("Arial", 10))
ans_label.grid(column=3, row=7)


def convert_miles_to_km():
    miles = float(input.get())
    kilometers = round(miles * 1.6, 2)
    ans_label.config(text=str(kilometers))


# Button
calculate_button = Button(text="Calculate", font=("Arial", 10), command=convert_miles_to_km)
calculate_button.grid(column=3, row=9)

window.mainloop()
