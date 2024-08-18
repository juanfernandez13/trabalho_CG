from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from lines import midpoint_algorithm
from curves import curvaHermite
from general import normalizer, scale_for_resolution

def forget(widgets):
    for widget in widgets:
        widget.pack_forget()

def retrieve(widget):
    widget.pack(side=LEFT, )

def menuView(addWidget, removeWidgets):
    retrieve(addWidget)
    forget(removeWidgets)

def getDataLines(points_entries, resolution, canvas):
    points = []

    for i in range(0, int(len(points_entries))):
        points.append((int(points_entries[i][0].get()), int(points_entries[i][1].get())))

    normalized_points = normalizer(points)
    scaled_points = scale_for_resolution(normalized_points, resolution)
    rasterized_points = []

    for i in range(0, len(scaled_points)-1):
        rasterized_points += midpoint_algorithm(scaled_points[i], scaled_points[i+1])

    plot_points2(rasterized_points, resolution, canvas)

def addEntryLines(points_frame, points_entries):
    row_count = len(points_entries)

    #entrada de pontos
    x_entry = Entry(points_frame, width=10)
    y_entry = Entry(points_frame, width=10)
    Label(points_frame, text=f"Ponto {row_count + 1} (x, y)").grid(row=row_count, column=0, padx=5, pady=5)
    x_entry.grid(row=row_count, column=1, padx=5, pady=5)
    y_entry.grid(row=row_count, column=2, padx=5, pady=5)
    points_entries.append((x_entry, y_entry))

def menuConfigLines(window, canvas):
    ViewMenuLines = Frame(window)

    #Frame de pontos
    points_entries = []

    points_frame = LabelFrame(ViewMenuLines, text="Pontos", padx=10, pady=10)
    points_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    #Inputs
    addEntryLines(points_frame, points_entries)
    addEntryLines(points_frame, points_entries)

    #botão adicionar botões
    Button(ViewMenuLines, text="Adicionar Pontos", command=lambda: addEntryLines(points_frame, points_entries)).grid(
        row=1, column=0, columnspan=4, pady=5)

    #Dropdown com resoluções
    resolutions = {
        "100x100": (100, 100),
        "300x300": (300, 300),
        "800x600": (800, 600),
        "1920x1080": (1920, 1080)
    }

    clicked = StringVar()
    clicked.set("100x100")
    Label(ViewMenuLines, text="Resolução atual:").grid(row=2, column=0, padx=5, pady=5)
    resolution_menu = OptionMenu(ViewMenuLines, clicked, *resolutions.keys())
    resolution_menu.grid(row=2, column=1, padx=5, pady=5)

    #Botão para plotar retas
    Button(ViewMenuLines, text="Plotar retas", command=lambda: getDataLines(points_entries, resolutions[clicked.get()], canvas))\
        .grid(row=3, column=0, columnspan=5, pady=10)

    return ViewMenuLines

def getDataCurves(points_entries,tangents_entries, num_points, resolution, canvas):
    points = []
    tangents = []

    for i in range(0, int(len(points_entries))):
        points.append((int(points_entries[i][0].get()), int(points_entries[i][1].get())))
        tangents.append((int(tangents_entries[i][0].get()), int(tangents_entries[i][1].get())))

    hermite_points = []
    for i in range(1, len(points)):
        hermite_points += curvaHermite(points[i-1], tangents[i-1], points[i], tangents[i], num_points)

    normalized_points = normalizer(hermite_points)
    scaled_points = scale_for_resolution(normalized_points, resolution)
    rasterized_points = []

    for i in range(0, len(scaled_points) - 1):
        rasterized_points += midpoint_algorithm(scaled_points[i], scaled_points[i + 1])

    plot_points2(rasterized_points, resolution, canvas)



def addEntryCurves(points_frame, points_entries, tangents_entries):
    row_count = len(points_entries)

    #entrada de pontos
    x_entry = Entry(points_frame, width=10,)
    y_entry = Entry(points_frame, width=10)
    Label(points_frame, text=f"Ponto {row_count + 1} (x, y)").grid(row=row_count + row_count , column=0, padx=5, pady=5)
    x_entry.grid(row=row_count + row_count, column=1, padx=5, pady=5)
    y_entry.grid(row=row_count + row_count, column=2, padx=5, pady=5)
    points_entries.append((x_entry, y_entry))

    #entrada de tangentes
    x_entry_t = Entry(points_frame, width=10)
    y_entry_t = Entry(points_frame, width=10)
    Label(points_frame, text=f"Tangente {row_count + 1} (x, y)").grid(row=row_count + row_count + 1, column=0, padx=5, pady=5)
    x_entry_t.grid(row=row_count + row_count + 1, column=1, padx=5, pady=5)
    y_entry_t.grid(row=row_count + row_count + 1, column=2, padx=5, pady=5)
    tangents_entries.append((x_entry_t, y_entry_t))

def menuConfigCurvas(window, canvas):
    ViewMenuCurvas = Frame(window)

    # Frame de pontos e tangentes
    points_entries = []
    tangents_entries = []

    data_frame = LabelFrame(ViewMenuCurvas, text="Pontos e tangentes", padx=10, pady=10)
    data_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    #Inputs de pontos e tangentes
    addEntryCurves(data_frame, points_entries, tangents_entries)
    addEntryCurves(data_frame, points_entries, tangents_entries)

    #Botão de adicionar input
    Button(ViewMenuCurvas, text="Adicionar Ponto e tangente", command=lambda: addEntryCurves(data_frame, points_entries,
        tangents_entries)).grid(row=1, column=0, columnspan=4, pady=5)

    #Dropdown para resoluções
    resolutions = {
        "100x100": (100, 100),
        "300x300": (300, 300),
        "800x600": (800, 600),
        "1920x1080": (1920, 1080)
    }
    clicked = StringVar()
    clicked.set("100x100")
    Label(ViewMenuCurvas, text="Resolução atual:").grid(row=2, column=0, padx=5, pady=5)
    resolution_menu = OptionMenu(ViewMenuCurvas, clicked, *resolutions)
    resolution_menu.grid(row=2, column=1, padx=5, pady=5)

    Label(ViewMenuCurvas, text="Quantidade de Segmentos").grid(row=3, column=0, padx=10, pady=5)
    num_segments_var = IntVar(value=5)
    Spinbox(ViewMenuCurvas, from_=1, to_=100, textvariable=num_segments_var).grid(row=3, column=1, padx=5,
                                                                                              pady=5)

    Button(ViewMenuCurvas, text="Plotar retas", command=lambda: getDataCurves(points_entries, tangents_entries,num_segments_var.get(), resolutions[clicked.get()], canvas)) \
        .grid(row=4, column=0, columnspan=5, pady=10)

    return ViewMenuCurvas


def menuConfigPolygon(window):
    ViewMenuPolygon = Frame(window)

    polygons = ['Triângulo Equilátero 1', 'Triângulo Equilátero 2', 'Quadrado 1', 'Quadrado 2', 'Hexágono 1','Hexágono 2']
    clicked = StringVar()
    clicked.set('Triângulo Equilátero 1')
    Label(ViewMenuPolygon, text="Escolha um poligono:").grid(row=0, column=0, padx=5, pady=5)
    polygons_menu = OptionMenu(ViewMenuPolygon, clicked, *polygons)
    polygons_menu.grid(row=1, column=0, padx=5, pady=5)

    resolutions = ["100x100", "300x300", "800x600", "1920x1080"]
    clicked = StringVar()
    clicked.set("100x100")
    Label(ViewMenuPolygon, text="Resolução atual:").grid(row=2, column=0, padx=5, pady=5)
    resolution_menu = OptionMenu(ViewMenuPolygon, clicked, *resolutions)
    resolution_menu.grid(row=3, column=0, padx=5, pady=5)

    return ViewMenuPolygon

def plot_points2(points, resolution, canvas):
    width, height = resolution
    img = np.ones((height + 1, width + 1))

    canvas.get_tk_widget().forget()

    for i in points:
        img[i[1]][i[0]] = 0

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)
    canvas.figure = fig
    canvas.draw()
    canvas.get_tk_widget().pack()


def view():
    window = Tk()
    window.title('Trabalho de CG')
    window.geometry("1200x900")
    menubar = Menu(window)
    menubar.add_command(label="lines", command=lambda: menuView(configLines, [configCurves, configPolygon]))
    menubar.add_command(label="Curves", command=lambda: menuView(configCurves, [configLines, configPolygon]))
    menubar.add_command(label="Poligonos", command=lambda: menuView(configPolygon, [configLines, configCurves]))

    control_frame = Frame(window)
    control_frame.pack(side=LEFT, anchor=NW)

    fig, ax = plt.subplots(figsize=(8, 8))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1, pady=4, padx=5)

    configLines = menuConfigLines(control_frame, canvas)
    configCurves = menuConfigCurvas(control_frame, canvas)
    configPolygon = menuConfigPolygon(control_frame)

    menuView(configLines, [configCurves, configPolygon])

    window.config(menu=menubar)
    window.mainloop()
