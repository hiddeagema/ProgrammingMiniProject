import base64
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import io

LARGE_FONT=("Verdana", 12)

class NSFietsenstalling(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "NS-Fietsenstalling")
        tk.Tk.wm_geometry(self,"700x455")       #fixed screen diameters
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, RegisterPage, StallPage, PickupPage, InfoPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#FFCC18')
        titelLabel = tk.Label(self, bg="#FFCC18", anchor=tk.W, justify=tk.LEFT, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        image = Image.open("NS.jpg")
        photoholder = ImageTk.PhotoImage(image)
        photo = tk.Label(self, image = photoholder)
        photo.image = photoholder
        photo.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        registerButton = tk.Button(self, height=5, width=23, justify=tk.LEFT, bg="#011466", fg="#FFFFFF", text="Registreer", command=lambda: controller.show_frame(RegisterPage))
        stallButton = tk.Button(self, height=5, width=25, justify=tk.LEFT, bg="#011466", fg="#FFFFFF", text="Stal fiets", command=lambda: controller.show_frame(StallPage))
        pickupButton = tk.Button(self, height=5, width=25, justify=tk.LEFT, bg="#011466", fg="#FFFFFF", text="Haal fiets op", command=lambda: controller.show_frame(PickupPage))
        infoButton = tk.Button(self, height=5, width=22, justify=tk.LEFT, bg="#011466", fg="#FFFFFF", text="Informatie opvragen", command=lambda: controller.show_frame(InfoPage))

        registerButton.pack(fill=tk.BOTH,side=tk.LEFT)
        stallButton.pack(fill=tk.BOTH,side=tk.LEFT)
        pickupButton.pack(fill=tk.BOTH,side=tk.LEFT)
        infoButton.pack(fill=tk.BOTH,side=tk.LEFT)

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class StallPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class PickupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='yellow')
        titelLabel = ttk.Label(self, text="NS-Fietsenstalling", font=LARGE_FONT)
        titelLabel.pack(pady=10, padx=10)

        homeButton = ttk.Button(self, text="Naar beginscherm", command=lambda: controller.show_frame(StartPage))
        homeButton.pack()

app = NSFietsenstalling()
app.mainloop()
