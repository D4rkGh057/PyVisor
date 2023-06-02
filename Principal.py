from tkinter import *
from Interfaz.Ventana import *


def main():
    root = Tk()
    root.title("Visor Imagen")
    app = Ventana(root)
    app.mainloop()


if __name__ == "__main__":
    main()
