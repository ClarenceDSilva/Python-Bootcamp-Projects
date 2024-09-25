from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas_front_img = PhotoImage(file='images/card_front.png')
tick_img = PhotoImage(file='images/right.png')
cross_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=canvas_front_img)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

unknown_button = Button(image=cross_img, highlightthickness=0)
unknown_button.grid(row=1, column=0)

known_button = Button(image=tick_img, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()

