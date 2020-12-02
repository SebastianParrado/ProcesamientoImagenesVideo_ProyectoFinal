# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:25:59 2020

@author: andre
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image # Para mostrar la imagen en la interfaz GUI
from PIL import ImageTk # Para mostrar la imagen en la interfaz GUI
import cv2
#import sys

###Step 1: Create The App Frame
class AppFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ###call the parent constructor
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
    
        # Variables globales
        self.image =  None  # Imagen
        self.state = True # Estado pantalla completa
        self.panelA = None # Panel A ventana
        self.panelB = None # Panel B ventana
        
        # Colores de la interfaz - Códigos de colores: https://htmlcolorcodes.com/es/
        """
        Morado
        
        self.but_bg = '#E188FD' # Fondo boton
        self.but_fg = '#55086D' # Letra boton
        self.wn_bg = '#F4E0FA'  # Fondo ventana
        self.wn_fg = '#55086D'  # Letra ventana
        """
        """
        Azul
        """
        self.but_bg = '#78CCEB' # Fondo boton
        self.but_fg = '#0B5E7D' # Letra boton
        self.wn_bg = '#E0F3FA'  # Fondo ventana
        self.wn_fg = '#0B5E7D'  # Letra ventana
        
        # self.tamanio imagenes que se muestran en la interfaz. Las imagenes son cuadradas
        self.tam = 600 
        
        # Posiciones y self.tamanios de los botones
        self.btn_posx = 1240 # Posicion x del boton
        self.btn_posy = 130 # Posicion y del primer bloque de botones
        self.btn_posy2 = 660 # Posicion y del segundo bloque de botones
        self.btn_w = 110 # self.tamanio horizontal boton
        self.btn_h = 30 # self.tamanio vertical boton
        
        """
        Textos en la ventana
        """
        lbl0 = tk.Label(self, text=" ", font=("Arial Bold", 40)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl0.place(x=0, y=0, width=1370, height=820) # Posicion y self.tamanio texto
        lbl0.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl1 = tk.Label(self, text="Procesamiento de imágenes", font=("Arial Bold", 40)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl1.place(x=10, y=20, width=1220, height=60) # Posicion y self.tamanio texto
        lbl1.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl2 = tk.Label(self, text="Acá iría la explicación del proyecto", font=("Arial Bold", 15)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl2.place(x=10, y=80, width=1220, height=30) # Posicion y self.tamanio texto
        lbl2.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        lbl3 = tk.Label(self, text="Proyecto realizado por: Pablo Mosquera, Juan Sebastián Parrado y Andrea Ruiz", font=("Arial Bold", 10)) # Configuracion boton (ventana, texto, estilo y self.tamaño de letra)
        lbl3.place(x=10, y=740, width=1220, height=30) # Posicion y self.tamanio texto
        lbl3.configure(bg=self.wn_bg,fg=self.wn_fg) # Colores texto
        
        """
        Botones en la ventana
        """
        n = 0 # Hace referencia a la operacion de la posicion en y del boton 1
        btn1 = tk.Button(self, text="Select an image", bg=self.but_bg, fg=self.but_fg, command=self.select_image) # Configuracion del boton 1 (ventana, texto, colores de fondo y de letra, funcion)
        btn1.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 1
        
        n = 1 # Hace referencia a la operacion de la posicion en y del boton 2
        btn2 = tk.Button(self, text="Rectangle", bg=self.but_bg, fg=self.but_fg, command=self.select_rectangle) # Configuracion del boton 2 (ventana, texto, colores de fondo y de letra, funcion)
        btn2.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 2
        
        n = 2 # Hace referencia a la operacion de la posicion en y del boton 3
        btn3 = tk.Button(self, text="Background", bg=self.but_bg, fg=self.but_fg, command=self.select_background) # Configuracion del boton 3 (ventana, texto, colores de fondo y de letra, funcion)
        btn3.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 3
        
        n = 3 # Hace referencia a la operacion de la posicion en y del boton 4
        btn4 = tk.Button(self, text="Foreground", bg=self.but_bg, fg=self.but_fg, command=self.select_foreground) # Configuracion del boton 4 (ventana, texto, colores de fondo y de letra, funcion)
        btn4.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 4
        
        n = 4 # Hace referencia a la operacion de la posicion en y del boton 5
        btn5 = tk.Button(self, text="Iteration", bg=self.but_bg, fg=self.but_fg, command=self.select_iteration) # Configuracion del boton 5 (ventana, texto, colores de fondo y de letra, funcion)
        btn5.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 5
        
        n = 5 # Hace referencia a la operacion de la posicion en y del boton 6
        btn6 = tk.Button(self, text="Select Background", bg=self.but_bg, fg=self.but_fg, command=self.select_bg) # Configuracion del boton 6 (ventana, texto, colores de fondo y de letra, funcion)
        btn6.place(x=self.btn_posx, y=(self.btn_posy+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 6
        
        # n = 0 # Hace referencia a la operacion de la posicion en y del boton 7
        # btn7 = tk.Button(self, text="Fullscreen", bg=self.but_bg, fg=self.but_fg, command=self.select_fs) # Configuracion del boton 7 (ventana, texto, colores de fondo y de letra, funcion)
        # btn7.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 7
        
        n = 1  # Hace referencia a la operacion de la posicion en y del boton 8
        btn8 = tk.Button(self, text="Exit", bg=self.but_bg, fg=self.but_fg, command=self.select_quit) # Configuracion del boton 8 (ventana, texto, colores de fondo y de letra, funcion)
        btn8.place(x=self.btn_posx, y=(self.btn_posy2+(n*40)), width=self.btn_w, height=self.btn_h) # Posicion y self.tamanio boton 8

        
        ###Create button
        #btn = tk.Button(self, text='askopenfilename',command=self.askopenfilename)
        #btn.pack(pady=5)

    def askopenfilename(self):
        ###ask filepath
        filepath = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))) # Abre el buscador de archivos

        ###if you selected a file path
        if filepath: # Verifica que se escoge un archivo y/o no se ha dado click en cancelar
            self.filepath = filepath    
        #image = cv2.imread(path) # load the image from disk
        #return image

    # Funcion de seleccionar imagen
    def select_image(self):
        print("ENTRO A SELECCIONAR IMAGEN")
        self.askopenfilename()
        self.image_in = cv2.imread(self.filepath) # load the image from disk
        self.image_out = cv2.imread(self.filepath) # load the image from disk
        self.image_in = cv2.resize(self.image_in,(self.tam,self.tam))
        self.image_out = cv2.resize(self.image_out,(self.tam,self.tam))
        self.trans_show_images()
        # self.image_in = self.askopenfilename
        # self.image_out = self.askopenfilename
    # Funcion para transformar y mostrar imagenes en GUI      
    def trans_show_images(self):
        # OpenCV represents images in BGR order; however PIL represents
  		# images in RGB order, so we need to swap the channels
        self.image_in = cv2.cvtColor(self.image_in, cv2.COLOR_BGR2RGB)
        self.image_out = cv2.cvtColor(self.image_out, cv2.COLOR_BGR2RGB)
  		# convert the images to PIL format...
        self.image_in = Image.fromarray(self.image_in)
        self.image_out = Image.fromarray(self.image_out)
  		# ...and then to ImageTk format
        self.image_in = ImageTk.PhotoImage(self.image_in)
        self.image_out = ImageTk.PhotoImage(self.image_out)
          
          # if the panels are None, initialize them
        if self.panelA is None or self.panelB is None:
            # the first panel will store our original imag
            self.panelA = tk.Label(image=self.image_in)
            self.panelA.image = self.image_in
            self.panelA.place(x=10, y=self.btn_posy, width=self.tam, height=self.tam)
            # while the second panel will store the edge map
            self.panelB = tk.Label(image=self.image_out)
            self.panelB.image = self.image_out       
            self.panelB.place(x=620, y=self.btn_posy, width=self.tam, height=self.tam)
            # otherwise, update the image panels
        else:
            # update the pannels
            self.panelA.configure(image=self.image_in)
            self.panelB.configure(image=self.image_out)
            self.panelA.image = self.image_in
            self.panelB.image = self.image_out
    
                
    # Funcion de hacer el rectangulo
    def select_rectangle(self):
        print("HOLA")  
    
    # Funcion para seleccionar fondo
    def select_background(self):
        print("HOLA BG")  
    
    # Funcion para seleccionar primer plano
    def select_foreground(self):
        print("HOLA FG")
    
    # Funcion para realizar iteracion
    def select_iteration(self):
        print("HOLA IT")
    
    # Funcion para seleccionar imagenes del fondo
    def select_bg(self):
        print("HOLA FG sel")
        self.askopenfilename()
        self.image_in = cv2.imread(self.filepath) # load the image from disk
        self.image_out = cv2.imread(self.filepath) # load the image from disk
        self.image_in = cv2.resize(self.image_in,(self.tam,self.tam))
        self.image_out = cv2.resize(self.image_out,(self.tam,self.tam))
        self.trans_show_images()
        
    # Funcion para seleccionar o quitar pantalla completa
    def select_fs(self):
        #global state # variables globales usadas
        if self.state: # Si esta en pantalla completa...
            self.state = False # ... salga de pantalla completa
        else: # Si no esta en pantalla completa...
            self.state = True # ... ponga pantalla completa
        self.attributes("-fullscreen", self.state) # Ajustar el estado de la pantalla
        
    # Funcion para cerrar la ventana
    def select_quit(self):
        #global window  # variables globales usadas
        self.destroy()
        #sys.exit()


###Step 2: Creating The App
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        ###call the parent constructor
        tk.Tk.__init__(self, *args, **kwargs)
        
         # Colores de la interfaz - Códigos de colores: https://htmlcolorcodes.com/es/
        """
        Morado
        
        self.but_bg = '#E188FD' # Fondo boton
        self.but_fg = '#55086D' # Letra boton
        self.wn_bg = '#F4E0FA'  # Fondo ventana
        self.wn_fg = '#55086D'  # Letra ventana
        """
        """
        Azul
        """
        self.but_bg = '#78CCEB' # Fondo boton
        self.but_fg = '#0B5E7D' # Letra boton
        self.wn_bg = '#E0F3FA'  # Fondo ventana
        self.wn_fg = '#0B5E7D'  # Letra ventana
        
        # self.tamanio imagenes que se muestran en la interfaz. Las imagenes son cuadradas
        self.tam = 600 
        
        # Posiciones y self.tamanios de los botones
        self.btn_posx = 1240 # Posicion x del boton
        self.btn_posy = 130 # Posicion y del primer bloque de botones
        self.btn_posy2 = 660 # Posicion y del segundo bloque de botones
        self.btn_w = 110 # self.tamanio horizontal boton
        self.btn_h = 30 # self.tamanio vertical boton
       
            
        self.attributes("-fullscreen", True) # Pantalla completa
        wn_bg = '#E0F3FA'  # Fondo ventana
        #tk.Tk(['bg'])=wn_bg
        self.configure(bg='#E0F3FA') # Color ventana

        ###create filepath list
        self.filepaths = []

        ###show app frame
        self.appFrame = AppFrame(self)
        self.appFrame.pack(side="top",fill="both",expand=True)
        
###Step 3: Bootstrap the app
def main():
    app = App()
    window = tk.Tk()
    """
    Configuracion de la ventana
    """
    #tk.title("Proyecto Procesamiento de Imagenes") # Titulo ventana
    #tk.geometry('1360x720') # self.tamaño ventana

    app.mainloop()

if __name__ == '__main__':
    main()