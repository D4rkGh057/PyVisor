from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from matplotlib.pyplot import title

win = Tk()
ruta = filedialog.askopenfilename(
    filetypes=[("image", ".jpg"), ("image", ".png"), ("image", ".jpeg")])
if len(ruta) > 0:
    global image
    # Leer la imagen de entrada y la redimensionamos
image = cv2.imread(ruta)
image = imutils.resize(image, height=380)
# Para visualizar la imagen de entrada en la GUI
imageToShow = imutils.resize(image, width=180)
im = Image.fromarray(imageToShow)
img = ImageTk.PhotoImage(image=im)
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(80, 80, image=img, anchor=CENTER)
win.mainloop()
