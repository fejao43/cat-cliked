from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pygame

window = tk.Tk()

pygame.mixer.init()

def button_music():
    pygame.mixer.music.load("/home/joaodev/Projetos/cat_cliked/song/miau.mp3")
    pygame.mixer.music.play()



image = Image.open("/home/joaodev/Imagens/_ (4).jpeg")

image_tk = ImageTk.PhotoImage(image)

cat = Button(window, image = image_tk,command=button_music)
cat.pack()




window.mainloop()