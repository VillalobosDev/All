import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont  
import pymysql
import csv
from datetime import datetime
import ctypes
from app_functions import *

def create_rounded_rectangle(canvas, x0, y0, x1, y1, r, **kwargs):
    """Draw a rounded rectangle on the specified canvas."""
    points = [
        x0 + r, y0,   # Top-left corner
        x1 - r, y0,   # Top-right corner
        x1, y0 + r,   # Top-right corner round
        x1, y1 - r,   # Bottom-right corner round
        x1 - r, y1,   # Bottom-right corner
        x0 + r, y1,   # Bottom-left corner
        x0, y1 - r,   # Bottom-left corner round
        x0, y0 + r,   # Top-left corner round
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Create the main window using customtkinter
window = ctk.CTk()
window.title("CRUD Catastro")
window.geometry("1330x600")
#window.resizable(width=False,height=False)

myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window.iconbitmap(r'C:\Users\Nelson\Desktop\Serv COM & Proyecto\Code\CatastroCRUD\img\img.ico')

# Create a frame for input fields and buttons
frame = ctk.CTkFrame(window)
frame.pack(fill="x", padx=10, pady=10)

# Buttons style
button_poppins = ("poppins", 16, "bold") 
placeholder_poppins = ("poppins", 12, "normal") 

# Create buttons aligned horizontally
buttons = [
    ("Agregar", save),
    ("Actualizar", update),
    ("Eliminar", delete),
    ("Buscar", find),
    ("Limpiar", clear),
    ("Exportar a Excel", exportExcel)
]

for i, (text, command) in enumerate(buttons):
    ctk.CTkButton(frame, text=text, command=command, font=button_poppins).grid(row=0, column=i, padx=5, pady=5, sticky="w")

# Create input fields with placeholders after the buttons
cedulaEntry = ctk.CTkEntry(frame, placeholder_text="Cedula", font=placeholder_poppins)
cedulaEntry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

contribuyenteEntry = ctk.CTkEntry(frame, placeholder_text="Contribuyente", font=placeholder_poppins)
contribuyenteEntry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

nombreinmuebleEntry = ctk.CTkEntry(frame, placeholder_text="Nombre Inmueble", font=placeholder_poppins)
nombreinmuebleEntry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

rifEntry = ctk.CTkEntry(frame, placeholder_text="RIF", font=placeholder_poppins)
rifEntry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

sectorEntry = ctk.CTkEntry(frame, placeholder_text="Sector", font=placeholder_poppins)
sectorEntry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

usoEntry = ctk.CTkEntry(frame, placeholder_text="Uso", font=placeholder_poppins)
usoEntry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

codcatastralEntry = ctk.CTkEntry(frame, placeholder_text="Cod Catastral", font=placeholder_poppins)
codcatastralEntry.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

fechaliquidacionEntry = ctk.CTkEntry(frame, placeholder_text="Fecha Liquidacion", font=placeholder_poppins)
fechaliquidacionEntry.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

# Create a frame to hold the Treeview
frame_tree = ctk.CTkFrame(window, fg_color='white', width=580, height=360)
frame_tree.pack(pady=10, padx=10, expand=True, fill="both")  # Adjusted padding

# Create a style for the Treeview
style = ttk.Style()
style.configure("Custom.Treeview", font=("Poppins", 12))  # Set the desired font and size for the treeview
style.configure("Custom.Treeview.Heading", font=("Poppins", 14, "bold"))  # Set header font size and style

# Create Treeview for displaying records with the custom style
my_tree = ttk.Treeview(frame_tree, style="Custom.Treeview", show="headings")
my_tree.pack(pady=10, padx=10, fill="both", expand=True)

# Define columns
my_tree['columns'] = ('cedula', 'contribuyente', 'nombreinmueble', 'rif', 'sector', 'uso', 'codcatastral', 'fechaliquidacion')

# Format columns
for col in my_tree['columns']:
    my_tree.heading(col, text=col.capitalize(), anchor='center')  # Ensure anchor alignment
    my_tree.column(col, anchor='center')

my_tree.bind('<ButtonRelease-1>', lambda event: select())  # Bind selection event

# Draw a rounded rectangle on the frame_tree
canvas = ctk.CTkCanvas(frame_tree, width=0, height=0, highlightthickness=0, bg='white')
canvas.place(x=0, y=0)  # Position the canvas at the top-left of the frame
create_rounded_rectangle(canvas, 10, 10, 0, 0, r=5, fill='lightgray', outline='black')

# Refresh the table
refreshTable(my_tree)

window.mainloop()














# import customtkinter as ctk
# from tkinter import ttk
# from tkinter import messagebox
# import tkinter.font as tkFont  
# import pymysql
# import csv
# from datetime import datetime
# import ctypes
# from app_functions import *

# def create_rounded_rectangle(canvas, x0, y0, x1, y1, r, **kwargs):
#     """Draw a rounded rectangle on the specified canvas."""
#     points = [
#         x0 + r, y0,   # Top-left corner
#         x1 - r, y0,   # Top-right corner
#         x1, y0 + r,   # Top-right corner round
#         x1, y1 - r,   # Bottom-right corner round
#         x1 - r, y1,   # Bottom-right corner
#         x0 + r, y1,   # Bottom-left corner
#         x0, y1 - r,   # Bottom-left corner round
#         x0, y0 + r,   # Top-left corner round
#     ]
#     return canvas.create_polygon(points, **kwargs, smooth=True)

# # Create the main window using customtkinter
# window = ctk.CTk()
# window.title("CRUD Catastro")
# window.geometry("1300x600")

# myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
# window.iconbitmap(r'C:\Users\Nelson\Desktop\Serv COM & Proyecto\Code\CatastroCRUD\img\img.ico')

# # Create a frame for input fields and buttons
# frame = ctk.CTkFrame(window)
# frame.pack(fill="x", padx=10, pady=10)

# # Buttons style
# button_poppins = ("poppins", 16, "bold") 
# placeholder_poppins = ("poppins", 12, "normal") 

# # Create buttons aligned horizontally
# buttons = [
#     ("Agregar", save),
#     ("Actualizar", update),
#     ("Eliminar", delete),
#     ("Buscar", find),
#     ("Limpiar", clear),
#     ("Exportar a Excel", exportExcel)
# ]

# for i, (text, command) in enumerate(buttons):
#     ctk.CTkButton(frame, text=text, command=command, font=button_poppins).grid(row=0, column=i, padx=5, pady=5, sticky="w")

# # Create input fields with placeholders after the buttons
# cedulaEntry = ctk.CTkEntry(frame, placeholder_text="Cedula", font=placeholder_poppins)
# cedulaEntry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# contribuyenteEntry = ctk.CTkEntry(frame, placeholder_text="Contribuyente", font=placeholder_poppins)
# contribuyenteEntry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

# nombreinmuebleEntry = ctk.CTkEntry(frame, placeholder_text="Nombre Inmueble", font=placeholder_poppins)
# nombreinmuebleEntry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# rifEntry = ctk.CTkEntry(frame, placeholder_text="RIF", font=placeholder_poppins)
# rifEntry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# sectorEntry = ctk.CTkEntry(frame, placeholder_text="Sector", font=placeholder_poppins)
# sectorEntry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# usoEntry = ctk.CTkEntry(frame, placeholder_text="Uso", font=placeholder_poppins)
# usoEntry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

# codcatastralEntry = ctk.CTkEntry(frame, placeholder_text="Cod Catastral", font=placeholder_poppins)
# codcatastralEntry.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

# fechaliquidacionEntry = ctk.CTkEntry(frame, placeholder_text="Fecha Liquidacion", font=placeholder_poppins)
# fechaliquidacionEntry.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

# # Create a frame to hold the Treeview with rounded corners
# frame_tree = ctk.CTkFrame(window, fg_color='white', width=580, height=360)
# frame_tree.pack(pady=10)  # Adjusted padding

# # Draw a rounded rectangle directly on the frame_tree
# canvas = ctk.CTkCanvas(frame_tree, width=580, height=360, highlightthickness=0, bg='white')
# canvas.pack(fill="both", expand=True)  # Use pack to fill the frame

# # Draw a rounded rectangle on the canvas
# create_rounded_rectangle(canvas, 10, 10, 3, 350, r=20, fill='lightgray', outline='black')

# # Create a style for the Treeview
# style = ttk.Style()
# style.configure("Custom.Treeview", font=("Poppins", 12))  # Set the desired font and size for the treeview
# style.configure("Custom.Treeview.Heading", font=("Poppins", 14, "bold"))  # Set header font size and style

# # Create Treeview for displaying records with the custom style
# my_tree = ttk.Treeview(frame_tree, style="Custom.Treeview", show="headings")  # Attach Treeview to frame_tree
# my_tree.pack(pady=20, padx=10, fill="both", expand=True)  # Use pack to fill the frame

# # Define columns
# my_tree['columns'] = ('cedula', 'contribuyente', 'nombreinmueble', 'rif', 'sector', 'uso', 'codcatastral', 'fechaliquidacion')

# # Format columns
# for col in my_tree['columns']:
#     my_tree.heading(col, text=col.capitalize(), anchor='center')  # Ensure anchor alignment
#     my_tree.column(col, anchor='center')

# my_tree.bind('<ButtonRelease-1>', lambda event: select())  # Bind selection event

# # Refresh the table
# refreshTable(my_tree)

# window.mainloop()









# # import customtkinter as ctk
# # from tkinter import ttk
# # from tkinter import messagebox
# # import tkinter.font as tkFont  
# # import pymysql
# # import csv
# # from datetime import datetime
# # import ctypes
# # from app_functions import *

# # def create_rounded_rectangle(canvas, x0, y0, x1, y1, r, **kwargs):
# #     """Draw a rounded rectangle on the specified canvas."""
# #     points = [
# #         x0 + r, y0,   # Top-left corner
# #         x1 - r, y0,   # Top-right corner
# #         x1, y0 + r,   # Top-right corner round
# #         x1, y1 - r,   # Bottom-right corner round
# #         x1 - r, y1,   # Bottom-right corner
# #         x0 + r, y1,   # Bottom-left corner
# #         x0, y1 - r,   # Bottom-left corner round
# #         x0, y0 + r,   # Top-left corner round
# #     ]
# #     return canvas.create_polygon(points, **kwargs, smooth=True)

# # # Create the main window using customtkinter
# # window = ctk.CTk()
# # window.title("CRUD Catastro")
# # window.geometry("1300x600")

# # myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
# # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
# # window.iconbitmap(r'C:\Users\Nelson\Desktop\Serv COM & Proyecto\Code\CatastroCRUD\img\img.ico')

# # # Create a frame for input fields and buttons
# # frame = ctk.CTkFrame(window)
# # frame.pack(fill="x", padx=10, pady=10)

# # # Buttons style
# # button_poppins = ("poppins", 16, "bold") 
# # placeholder_poppins = ("poppins", 12, "normal") 

# # # Create buttons aligned horizontally
# # buttons = [
# #     ("Agregar", save),
# #     ("Actualizar", update),
# #     ("Eliminar", delete),
# #     ("Buscar", find),
# #     ("Limpiar", clear),
# #     ("Exportar a Excel", exportExcel)
# # ]

# # for i, (text, command) in enumerate(buttons):
# #     ctk.CTkButton(frame, text=text, command=command, font=button_poppins).grid(row=0, column=i, padx=5, pady=5, sticky="w")

# # # Create input fields with placeholders after the buttons
# # cedulaEntry = ctk.CTkEntry(frame, placeholder_text="Cedula", font=placeholder_poppins)
# # cedulaEntry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# # contribuyenteEntry = ctk.CTkEntry(frame, placeholder_text="Contribuyente", font=placeholder_poppins)
# # contribuyenteEntry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

# # nombreinmuebleEntry = ctk.CTkEntry(frame, placeholder_text="Nombre Inmueble", font=placeholder_poppins)
# # nombreinmuebleEntry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# # rifEntry = ctk.CTkEntry(frame, placeholder_text="RIF", font=placeholder_poppins)
# # rifEntry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# # sectorEntry = ctk.CTkEntry(frame, placeholder_text="Sector", font=placeholder_poppins)
# # sectorEntry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

# # usoEntry = ctk.CTkEntry(frame, placeholder_text="Uso", font=placeholder_poppins)
# # usoEntry.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

# # codcatastralEntry = ctk.CTkEntry(frame, placeholder_text="Cod Catastral", font=placeholder_poppins)
# # codcatastralEntry.grid(row=7, column=0, padx=5, pady=5, sticky="ew")

# # fechaliquidacionEntry = ctk.CTkEntry(frame, placeholder_text="Fecha Liquidacion", font=placeholder_poppins)
# # fechaliquidacionEntry.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

# # # Create a canvas for the rounded rectangle
# # canvas = ctk.CTkCanvas(window, width=580, height=380, highlightthickness=0)
# # canvas.pack(pady=20)

# # # Draw a rounded rectangle on the canvas
# # create_rounded_rectangle(canvas, 10, 10, 570, 370, r=20, fill='lightgray', outline='black')

# # # Create a frame to hold the Treeview with specified dimensions
# # frame_tree = ctk.CTkFrame(window, fg_color='white', width=580, height=360)
# # frame_tree.pack(pady=20)  # Use pack instead of place

# # # Create a style for the Treeview
# # style = ttk.Style()
# # style.configure("Custom.Treeview", font=("Poppins", 12))  # Set the desired font and size for the treeview
# # style.configure("Custom.Treeview.Heading", font=("Poppins", 14, "bold"))  # Set header font size and style

# # # Create Treeview for displaying records with the custom style
# # my_tree = ttk.Treeview(frame_tree, style="Custom.Treeview", show="headings")
# # my_tree.pack(pady=20, padx=10, fill="both", expand=True)

# # # Define columns
# # my_tree['columns'] = ('cedula', 'contribuyente', 'nombreinmueble', 'rif', 'sector', 'uso', 'codcatastral', 'fechaliquidacion')

# # # Format columns
# # for col in my_tree['columns']:
# #     my_tree.heading(col, text=col.capitalize(), anchor='center')  # Ensure anchor alignment
# #     my_tree.column(col, anchor='center')

# # my_tree.bind('<ButtonRelease-1>', lambda event: select())  # Bind selection event

# # refreshTable(my_tree)

# # window.mainloop()