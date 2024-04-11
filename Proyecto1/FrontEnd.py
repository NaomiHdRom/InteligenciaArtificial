from tkinter import*
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import main as cu

def buscar(etiquetaTrayectoria):
    #PRIMERO OBTENEMOS EL DATO QUE EL USUARIO SELECCIONO DE ORIGEN Y DESTINO
    origen= input_origen.get()

    destino= input_destino.get()

    G1 = cu.principal(cu.Grafo)  # Creación del objeto tipo grafo  
    ciudad = G1.costo_uniforme(origen, destino)  # Devuelve la ciudad encontrada 
    # Guardar la trayectoria y su costo
    trayectoria = []
    costo_total = ciudad.costo
    while ciudad.padre is not None:
        trayectoria.append(ciudad.name)
        ciudad = ciudad.padre
    trayectoria.reverse()  # Revertir la trayectoria para que esté en el orden correcto
    
    # Actualizar el texto del Label con la nueva trayectoria y su costo
    trayectoria_texto = " -> ".join(trayectoria)
    etiquetaTrayectoria.config(text="Trayectoria: "+ origen +" -> " + trayectoria_texto + " (Costo total: " + str(costo_total) + ")")




# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Búsqueda Uniforme: Rumania")

#AÑADIR LABELS, BOTONES, ETC
    # Crear un frame para contener la etiqueta, menús y botón
top_frame = Frame(root)
top_frame.pack()

# Crear la etiqueta de origen
etiquetaOrigen = Label(top_frame, text="Origen:")
etiquetaOrigen.grid(row=0, column=0)

# Crear la etiqueta de destino
etiquetaDestino = Label(top_frame, text="Destino:")
etiquetaDestino.grid(row=0, column=1)

# Opciones para los menús desplegables
ciudades = [
    "Arad",
    "Bucharest",
    "Craiova",
    "Dobreta",
    "Eforie",
    "Fagaras",
    "Giurgiu",
    "Hirsova",
    "Iasi",
    "Lugoj",
    "Mehadia",
    "Neamt",
    "Pitesti",
    "Rimnicu Vilcea",
    "Oradea",
    "Sibiu",
    "Timisoara",
    "Urziceni",
    "Vaslui",
    "Zerind",
]

# Variables para la selección de origen y destino
input_origen = StringVar()
input_origen.set(ciudades[0])  # Valor predeterminado para el menú de origen
input_destino = StringVar()
input_destino.set(ciudades[1])  # Valor predeterminado para el menú de destino
                            #Para obtener el dato de la ciudad seleccionada se usa origen/destino.get()

# Menú desplegable para la selección de origen
selecOrigen = OptionMenu(top_frame, input_origen, *ciudades)
selecOrigen.grid(row=1, column=0)

# Menú desplegable para la selección de destino
selecDestino = OptionMenu(top_frame, input_destino, *ciudades)
selecDestino.grid(row=1, column=1)

# Crear el botón de búsqueda
#######################################
#METODO UNIFORME
# Mandamos a llamar la funcion de buscar 
boton = Button(top_frame, text="Buscar", command=lambda: buscar(etiquetaTrayectoria))
#Agrege command para que detecte el clik 
boton.grid(row=1, column=2)

# Crear un frame a la izq
left_frame = Frame(root)
left_frame.pack(side="left", padx=10, pady=10)

etiquetaRuta = Label(left_frame, text="Ruta:")
etiquetaRuta.grid(row=0, column=0)

etiquetaTrayectoria = Label(left_frame)
etiquetaTrayectoria.grid(row=1, column=0)    
    


#Crear un frame para las etiquetas abajo de la imagen
bot_frame = Frame(root)
bot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

# Crear la etiqueta de Nombre de los integrantes
etiquetaUNAM = Label(bot_frame, text="Universidad Nacional Autónoma de México   |  Facultad de Ingeniería")
etiquetaUNAM.grid(row=0, column=0)

# Crear la etiqueta de Nombre del Proyecto
etiquetaIntegrantes = Label(bot_frame, text="Inteligencia Artificial: Proyecto 1")
etiquetaIntegrantes.grid(row=1, column=0)

# Crear la etiqueta de Nombre de los integrantes
etiquetaIntegrantes = Label(bot_frame, text="INTEGRANTES:")
etiquetaIntegrantes.grid(row=0, column=2,)
etiquetaIntegrantes1 = Label(bot_frame, text="          Naomi Estefanía Hernández Romero")
etiquetaIntegrantes1.grid(row=1, column=2,sticky="e")
etiquetaIntegrantes2 = Label(bot_frame, text="          Olivera Parias Pedro Eduardo")
etiquetaIntegrantes2.grid(row=2, column=2)

#################################################################################
# Crear el lienzo de Matplotlib en Tkinter
fig = plt.figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear el gráfico de NetworkX


G = nx.Graph()
G.add_nodes_from(['Arad','Bucharest','Craiova','Dobreta','Eforie','Fagaras','Giurgiu','Hirsova','Iasi','Lugoj','Mehadia','Neamt','Oradea','Pitesti','Rimnicu Vilcea','Sibiu','Timisoara','Urziceni','Vaslui','Zerind'])

position = {
    "Oradea": (-5.32, 37.1),
    "Zerind": (-11.94, 28.3),
    "Arad": (-12.39, 13.47),
    "Sibiu": (0.07, 14.7),
    "Fagaras": (14.08, 8.8),
    "Timisoara": (-9.34, -3.6),
    "Lugoj": (-1.16, -10.2),
    "Mehadia": (-0.5, -23.38),
    "Dobreta": (-2.92, -35),
    "Rimnicu Vilcea": (3.44, -3.3),
    "Pitesti": (11.19, -7.16),
    "Craiova": (6.40, -27.3),
    "Bucharest": (20, -10),
    "Giurgiu": (19.21, -24.12),
    "Urziceni": (27.98, -4.35),
    "Vaslui": (29.93, 15.6),
    "Iasi": (25.31, 29.8),
    "Neamt": (18.58, 33.7),
    "Hirsova": (35, -4.35),
    "Eforie": (38.21, -17)
    
        #Para acceder al dato y usarlo mas adelante en codigo G.nodes["A"] o G.edges["A"]
}

G.add_edges_from([
    ("Oradea", "Zerind", {"distancia": 71}),
    ("Oradea", "Sibiu", {"distancia": 151}),
    ("Zerind", "Arad", {"distancia": 75}),
    ("Arad", "Sibiu", {"distancia": 140}),
    ("Arad", "Timisoara", {"distancia": 118}),
    ("Sibiu", "Rimnicu Vilcea", {"distancia": 80}),
    ("Sibiu", "Fagaras", {"distancia": 99}),
    ("Fagaras", "Bucharest", {"distancia": 211}),
    ("Timisoara", "Lugoj", {"distancia": 111}),
    ("Lugoj", "Mehadia", {"distancia": 70}),
    ("Mehadia", "Dobreta", {"distancia": 75}),
    ("Dobreta", "Craiova", {"distancia": 120}),
    ("Rimnicu Vilcea", "Craiova", {"distancia": 146}),
    ("Rimnicu Vilcea", "Pitesti", {"distancia": 97}),
    ("Pitesti", "Craiova", {"distancia": 138}),
    ("Pitesti", "Bucharest", {"distancia": 101}),
    ("Bucharest", "Giurgiu", {"distancia": 90}),
    ("Bucharest", "Urziceni", {"distancia": 85}),
    ("Urziceni", "Hirsova", {"distancia": 98}),
    ("Urziceni", "Vaslui", {"distancia": 142}),
    ("Vaslui", "Iasi", {"distancia": 92}),
    ("Iasi", "Neamt", {"distancia": 87}),
    ("Hirsova", "Eforie", {"distancia": 86})
])

edge_labels = {(u, v): d["distancia"] for u, v, d in G.edges(data=True)}

nx.draw(G, pos=position, with_labels=True, node_color="gray", node_size=1000,
        font_color="white", font_size=8, font_family="Times New Roman",
        font_weight="bold", width=5, ax=fig.gca())

nx.draw_networkx_edge_labels(G, pos=position, edge_labels=edge_labels,
                            font_size=6, label_pos=0.5, ax=fig.gca())




plt.margins(0.1)

# Actualiza el canvas de Tkinter
canvas.draw()



#######################################
#METODO UNIFORME

#PRIMERO OBTENEMOS EL DATO QUE EL USUARIO SELECCIONO DE ORIGEN Y DESTINO


#Ahora obtenemos los nodos conectados al origen
#nodos_conectados = list(G.neighbors(origen))
#nodos_conectados.sort()
# Imprimir los nodos conectados
#print("Nodos conectados al origen", origen, ":", nodos_conectados)



# Ejecutar el bucle principal de Tkinter
root.mainloop()


     


#def main(): 

    
    
  
    
#if __name__ == "__main__":
#    main()
    