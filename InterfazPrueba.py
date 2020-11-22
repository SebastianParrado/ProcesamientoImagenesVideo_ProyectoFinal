# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:56:45 2020

@author: sebas
"""

# import the necessary packages
from tkinter import *
from PIL import Image # Para mostrar la imagen en la interfaz GUI
from PIL import ImageTk # Para mostrar la imagen en la interfaz GUI
from tkinter import filedialog # Para buscar imagenes en el sistema
import cv2

window = Tk()

image =  None
state = True

"""
Morado

but_bg = '#E188FD'
but_fg = '#55086D'
wn_bg = '#F4E0FA'
wn_fg = '#55086D'
"""
"""
Azul
"""
but_bg = '#78CCEB'
but_fg = '#0B5E7D'
wn_bg = '#E0F3FA'
wn_fg = '#0B5E7D'

# Tamanio imagenes que se muestran en la interfaz. Las imagenes son cuadradas
tam = 600

btn_posx = 1240
btn_posy = 130
btn_posy2 = 660
btn_w = 110
btn_h = 30

def select_image():
	# grab a reference to the image panels
    global panelA, panelB, image
# kick off the GUI
	# open a file chooser dialog and allow the user to select an input
	# image
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) # Abre el buscador de archivos
    path = window.filename
# ensure a file path was selected
    if len(path) > 0: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises para hallar bordes
        edged = cv2.Canny(gray, 50, 100)
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
		# ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
			# the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.place(x=10, y=btn_posy, width=tam, height=tam)
			# while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged       
            panelB.place(x=620, y=btn_posy, width=tam, height=tam)
		# otherwise, update the image panels
        else:
			# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
            

def select_rectangle():
    print("HOLA")  

def select_background():
    print("HOLA BG")  

def select_foreground():
    print("HOLA FG")

def select_bg():
    print("HOLA FG")
    	# grab a reference to the image panels
    global panelA, panelB, image
# kick off the GUI
	# open a file chooser dialog and allow the user to select an input
	# image
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) # Abre el buscador de archivos
    path = window.filename
# ensure a file path was selected
    if len(path) > 0: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
        image = cv2.imread(path)
        edged = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Se convierte la imagen a escala de grises para hallar bordes
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
		# ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)
        
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
			# the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image     
            panelA.place(x=10, y=btn_posy, width=tam, height=tam)
			# while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged   
            panelB.place(x=620, y=btn_posy, width=tam, height=tam)
		# otherwise, update the image panels
        else:
			# update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged
            

def select_fs():
    global state
    if state:
        state = False
    else:
        state = True
    window.attributes("-fullscreen", state)
    
def select_quit():
    global window
    window.destroy()
            
# initialize the window toolkit along with the two image panels
panelA = None
panelB = None

window.title("Proyecto Procesamiento de Imagenes")
window.geometry('1360x720')
window.attributes("-fullscreen", state)
#set window color
window.configure(bg=wn_bg)
#window['background']='#FE6544'
lbl1 = Label(window, text="Procesamiento de imágenes", font=("Arial Bold", 40))
lbl1.place(x=10, y=20, width=1220, height=60)
lbl1.configure(bg=wn_bg,fg=wn_fg)

lbl2 = Label(window, text="Acá iría la explicación del proyecto", font=("Arial Bold", 15))
lbl2.place(x=10, y=80, width=1220, height=30)
lbl2.configure(bg=wn_bg,fg=wn_fg)

lbl3 = Label(window, text="Proyecto realizado por: Pablo Mosquera, Juan Sebastián Parrado y Andrea Ruiz", font=("Arial Bold", 10))
lbl3.place(x=10, y=740, width=1220, height=30)
lbl3.configure(bg=wn_bg,fg=wn_fg)
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
n = 0
btn1 = Button(window, text="Select an image", bg=but_bg, fg=but_fg, command=select_image)
btn1.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h)

n = 1
btn2 = Button(window, text="Rectangle", bg=but_bg, fg=but_fg, command=select_rectangle)
btn2.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h)

n = 2
btn3 = Button(window, text="Background", bg=but_bg, fg=but_fg, command=select_background)
btn3.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h)

n = 3
btn4 = Button(window, text="Foreground", bg=but_bg, fg=but_fg, command=select_foreground)
btn4.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h)

n = 4
btn5 = Button(window, text="Select Background", bg=but_bg, fg=but_fg, command=select_bg)
btn5.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h)

n = 0
btn6 = Button(window, text="Fullscreen", bg=but_bg, fg=but_fg, command=select_fs)
btn6.place(x=btn_posx, y=(btn_posy2+(n*40)), width=btn_w, height=btn_h)

n = 1
btn7 = Button(window, text="Exit", bg=but_bg, fg=but_fg, command=select_quit)
btn7.place(x=btn_posx, y=(btn_posy2+(n*40)), width=btn_w, height=btn_h)


# kick off the GUI
window.mainloop()