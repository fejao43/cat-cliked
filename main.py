from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pygame

window = tk.Tk()
window.title("cat-cliked")
window.geometry("500x500")
pygame.mixer.init()

def button_music():
    pygame.mixer.music.load("/home/joaodev/Projetos/cat_cliked/song/miau.mp3")
    pygame.mixer.music.play()



image = Image.open("/home/joaodev/Projetos/cat_cliked/picture/miaiauuu.jpeg")

image_tk = ImageTk.PhotoImage(image)

texto = Label(window, text="clique abaixo na foto na foto:")
texto.pack()

cat = Button(window,image = image_tk,command=button_music)
cat.pack()




window.mainloop()