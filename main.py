from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("restuarant")
window.geometry("500x500")
menu = {
    "Pizza":40,
    "Pasta":40,
    "Chocolate milk":7,
    "Ice cream cone":8,
    "Burger":20,
    "Fries":15,
    "Soda":15,
    "Milkshake":15   
}

label = Label(window, text = "Welcome to our restuarant")
label.pack()
frame = Frame(window)
frame.pack()

entries = {}
for item, price in menu.items():
  label = Label(frame, text=f"{item} - ${price:.2f}")
  label.pack(anchor='w')
  entry = Entry(frame, width=5)
  entry.pack(anchor='e')
  entries[item] = entry

def calculate_total():
  total = 0
  for item, entry in entries.items():
   quantity = entry.get()
   if quantity.isdigit():
     total += int(quantity) * menu[item]
     messagebox.showinfo("Total Bill", f"Your total bill is: ${total:.2f}")
     
     
button = Button(window, text = "calculate bill", command = calculate_total)
button.pack()

window.mainloop        