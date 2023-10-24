import random
import tkinter as tk


def generate_random_number():
    a = int(donja.get())
    b = int(gornja.get())

    if b <= a:
        rezultat.config(text="Gornja granica mora bit veca od donje")
    else:
        random_number = random.randint(a, b)
        rezultat.config(text=f"Random broj je : {random_number}")



app = tk.Tk()
app.title("Random Number Generator")


dole = tk.Label(app, text="Donja granica (a):")
dole.pack()
donja = tk.Entry(app)
donja.pack()

gore = tk.Label(app, text="Gornja Granica (b):")
gore.pack()
gornja = tk.Entry(app)
gornja.pack()


generate_button = tk.Button(app, text="Generisi", command=generate_random_number)
generate_button.pack()


rezultat = tk.Label(app, text="")
rezultat.pack()


app.mainloop()