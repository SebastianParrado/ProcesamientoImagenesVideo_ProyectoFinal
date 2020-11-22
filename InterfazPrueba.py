# -*- coding: utf-8 -*-
# import the necessary packages
from tkinter import *
from PIL import Image # Para mostrar la imagen en la interfaz GUI
from PIL import ImageTk # Para mostrar la imagen en la interfaz GUI
from tkinter import filedialog # Para buscar imagenes en el sistema
import cv2

window = Tk()

# Variables globales
image =  None  # Imagen
state = True # Estado pantalla completa
panelA = None # Panel A ventana
panelB = None # Panel B ventana

# Colores de la interfaz - Códigos de colores: https://htmlcolorcodes.com/es/
"""
Morado

but_bg = '#E188FD' # Fondo boton
but_fg = '#55086D' # Letra boton
wn_bg = '#F4E0FA'  # Fondo ventana
wn_fg = '#55086D'  # Letra ventana
"""
"""
Azul
"""
but_bg = '#78CCEB' # Fondo boton
but_fg = '#0B5E7D' # Letra boton
wn_bg = '#E0F3FA'  # Fondo ventana
wn_fg = '#0B5E7D'  # Letra ventana

# Tamanio imagenes que se muestran en la interfaz. Las imagenes son cuadradas
tam = 600 

# Posiciones y tamanios de los botones
btn_posx = 1240 # Posicion x del boton
btn_posy = 130 # Posicion y del primer bloque de botones
btn_posy2 = 660 # Posicion y del segundo bloque de botones
btn_w = 110 # Tamanio horizontal boton
btn_h = 30 # Tamanio vertical boton

# Funcion de seleccionar imagen
def select_image():
    # grab a reference to the image panels
    global panelA, panelB, image
# kick off the GUI
    # open a file chooser dialog and allow the user to select an input image
    window.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) # Abre el buscador de archivos
    path = window.filename
    # ensure a file path was selected
    if len(path) > 0: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
        image = cv2.imread(path) # load the image from disk
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
            
# Funcion de hacer el rectangulo
def select_rectangle():
    print("HOLA")  

# Funcion para seleccionar fondo
def select_background():
    print("HOLA BG")  

# Funcion para seleccionar primer plano
def select_foreground():
    print("HOLA FG")

# Funcion para realizar iteracion
def select_iteration():
    print("HOLA IT")

# Funcion para seleccionar imagenes del fondo
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
            
# Funcion para seleccionar o quitar pantalla completa
def select_fs():
    global state # variables globales usadas
    if state: # Si esta en pantalla completa...
        state = False # ... salga de pantalla completa
    else: # Si no esta en pantalla completa...
        state = True # ... ponga pantalla completa
    window.attributes("-fullscreen", state) # Ajustar el estado de la pantalla
    
# Funcion para cerrar la ventana
def select_quit():
    global window  # variables globales usadas
    window.destroy()

"""
Configuracion de la ventana
"""
window.title("Proyecto Procesamiento de Imagenes") # Titulo ventana
window.geometry('1360x720') # Tamaño ventana
window.attributes("-fullscreen", state) # Pantalla completa
window.configure(bg=wn_bg) # Color ventana

"""
Textos en la ventana
"""
lbl1 = Label(window, text="Procesamiento de imágenes", font=("Arial Bold", 40)) # Configuracion boton (ventana, texto, estilo y tamaño de letra)
lbl1.place(x=10, y=20, width=1220, height=60) # Posicion y tamanio texto
lbl1.configure(bg=wn_bg,fg=wn_fg) # Colores texto

lbl2 = Label(window, text="Acá iría la explicación del proyecto", font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y tamaño de letra)
lbl2.place(x=10, y=80, width=1220, height=30) # Posicion y tamanio texto
lbl2.configure(bg=wn_bg,fg=wn_fg) # Colores texto

lbl3 = Label(window, text="Proyecto realizado por: Pablo Mosquera, Juan Sebastián Parrado y Andrea Ruiz", font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y tamaño de letra)
lbl3.place(x=10, y=740, width=1220, height=30) # Posicion y tamanio texto
lbl3.configure(bg=wn_bg,fg=wn_fg) # Colores texto

"""
Botones en la ventana
"""
n = 0 # Hace referencia a la operacion de la posicion en y del boton 1
btn1 = Button(window, text="Select an image", bg=but_bg, fg=but_fg, command=select_image) # Configuracion del boton 1 (ventana, texto, colores de fondo y de letra, funcion)
btn1.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 1

n = 1 # Hace referencia a la operacion de la posicion en y del boton 2
btn2 = Button(window, text="Rectangle", bg=but_bg, fg=but_fg, command=select_rectangle) # Configuracion del boton 2 (ventana, texto, colores de fondo y de letra, funcion)
btn2.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 2

n = 2 # Hace referencia a la operacion de la posicion en y del boton 3
btn3 = Button(window, text="Background", bg=but_bg, fg=but_fg, command=select_background) # Configuracion del boton 3 (ventana, texto, colores de fondo y de letra, funcion)
btn3.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 3

n = 3 # Hace referencia a la operacion de la posicion en y del boton 4
btn4 = Button(window, text="Foreground", bg=but_bg, fg=but_fg, command=select_foreground) # Configuracion del boton 4 (ventana, texto, colores de fondo y de letra, funcion)
btn4.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 4

n = 4 # Hace referencia a la operacion de la posicion en y del boton 5
btn5 = Button(window, text="Iteration", bg=but_bg, fg=but_fg, command=select_iteration) # Configuracion del boton 5 (ventana, texto, colores de fondo y de letra, funcion)
btn5.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 5

n = 5 # Hace referencia a la operacion de la posicion en y del boton 6
btn6 = Button(window, text="Select Background", bg=but_bg, fg=but_fg, command=select_bg) # Configuracion del boton 6 (ventana, texto, colores de fondo y de letra, funcion)
btn6.place(x=btn_posx, y=(btn_posy+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 6

n = 0 # Hace referencia a la operacion de la posicion en y del boton 7
btn7 = Button(window, text="Fullscreen", bg=but_bg, fg=but_fg, command=select_fs) # Configuracion del boton 7 (ventana, texto, colores de fondo y de letra, funcion)
btn7.place(x=btn_posx, y=(btn_posy2+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 7

n = 1  # Hace referencia a la operacion de la posicion en y del boton 8
btn8 = Button(window, text="Exit", bg=but_bg, fg=but_fg, command=select_quit) # Configuracion del boton 8 (ventana, texto, colores de fondo y de letra, funcion)
btn8.place(x=btn_posx, y=(btn_posy2+(n*40)), width=btn_w, height=btn_h) # Posicion y tamanio boton 8

# kick off the GUI
window.mainloop()
