from io import BufferedIOBase
from re import A
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils


class Ventana(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=600, height=600)
        self.master = master
        self.pack()
        self.create_widgets()

    def open(self, frame1):
        self = None

        ruta = filedialog.askopenfilename(
            filetypes=[("image", ".jpg"), ("image", ".png"), ("image", ".jpeg")])
        if len(ruta) > 0:
            global image
        # Leer la imagen de entrada y la redimensionamos
        image = cv2.imread(ruta)
        image = imutils.resize(image, height=380)
        # Para visualizar la imagen de entrada en la GUI
        imageToShow = imutils.resize(image, width=180)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage = Label(frame1)
        lblInputImage.place(x=150, y=50)
        lblInputImage.configure(image=img)
        lblInputImage.image = img
        lblInputImage.pack()

    def create_widgets(self):
        # se agregan los frames donde serán colocados el boton de insert y los campos para insertar
        frame1 = Frame(self, bg="#726eff")
        frame1.place(x=0, y=0, width=600, height=600)
        lbl1 = Label(frame1, text="Seleccionar Imagen: ", bg="#726eff")
        lbl1.place(x=200, y=0)
        btnGuardar = Button(
            frame1, text="Buscar", command=self.open(frame1), bg="#37465b", fg="white")
        btnGuardar.place(x=310, y=0)
