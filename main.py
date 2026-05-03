from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()

image = Image.open("/home/joaodev/Imagens/_ (4).jpeg")

image_tk = ImageTk.PhotoImage(image)

label = Label(window, image = image_tk)
label.pack()

window = tk.Tk()



window.mainloop()