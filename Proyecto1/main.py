'''
    Desarrollado por:  
    * Hernández Romero Naomi Estefanía
    * Olivera Parias Pedro Eduardo
'''
import copy 
class Vertice: #Creacion de objetos tipo nodo 
    def __init__(self, nombre):
        self.name = nombre
        self.vecinos = []
        self.visitado= 'SV'
        self.costo = 0
        self.padre = None

    def add_vecino(self,nodo,costo):
        self.vecinos.append([nodo,costo])

    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    

class Grafo:
    def __init__(self): #Constructor: Creacion de nuestro diccionario
        self.ciudades={}
    
    def add_ciudad(self,newCiud): # Añadendo los nodos y su lista vacia 'conexiones'
        if newCiud in self.ciudades:
            return "Ciudad ya existente"
        ciudad = Vertice(newCiud)
        self.ciudades[newCiud]= ciudad

    def add_conex(self,nombreCit1,nombreCit2, costo): #Agregando conexion de ciudades  
        if nombreCit1 not in self.ciudades:
            raise ValueError('La ciudad "'+ nombreCit1 +'" no existe')
        if nombreCit2 not in self.ciudades:
            raise ValueError('La ciudad "'+ nombreCit2 +'" no existe')
        
        ciudad1 = self.ciudades[nombreCit1]  
        ciudad2 = self.ciudades[nombreCit2]
        
        ciudad1.add_vecino(ciudad2,costo)
        ciudad2.add_vecino(ciudad1,costo)

    def imprimir_grafo(self):
        lista= ''
        for cit in self.ciudades:
            lista += self.ciudades[cit].name+'-->'
            for vecino in self.ciudades[cit].vecinos:
                lista += '( '+ vecino[0].name +', '+str(vecino[1])+')'+ ','
            lista +='\n' 
        print(lista)

    def costo_uniforme(self,ciudadIni,meta): 
        ciudad = copy.deepcopy(self.ciudades[ciudadIni])
        ciudad.costo=0
        ciudad.padre = None
        cola= []
        cola.append(ciudad)
        print(len(cola))
        while len(cola) != 0:
            cola.sort(key=lambda x:x.name)
            if len(cola)==1:
                ciudadActual = cola.pop(0)
            elif cola[0].name == cola[1].name:
                if cola[0].costo > cola[1].costo:
                    del cola[0]
                    cola.sort(key=lambda x:x.costo)
                    ciudadActual = cola.pop(0)
                else:
                    cola[0],cola[1]=cola[1],cola[0]
                    del cola[0]
                    cola.sort(key=lambda x:x.costo)
                    ciudadActual = cola.pop(0)
            else:
                cola.sort(key=lambda x:x.costo)
                ciudadActual = cola.pop(0)
        
            print(ciudadActual.name)
            if not ciudadActual.name == self.ciudades[meta].name:
                for vecino in ciudadActual.vecinos: 
                    if ciudadActual.padre == None:
                        vecino1=copy.deepcopy(vecino[0])
                        vecino1.costo = vecino[1] + ciudadActual.costo
                        print('\t--->'+vecino[0].name+'\tcosto: '+str(vecino1.costo))
                        ciudadActual.visitado ='V'
                        vecino1.padre = ciudadActual
                        cola.append(vecino1) 
                    elif vecino[0].name == ciudadActual.padre.name:
                        #print(vecino1.name+' = '+ciudadActual.padre.name)
                        continue
                    else:
                        vecino1=copy.deepcopy(vecino[0])
                        vecino1.costo = vecino[1] + ciudadActual.costo
                        print('\t--->'+vecino[0].name+'\tcosto: '+str(vecino1.costo))
                        ciudadActual.visitado ='V'
                        vecino1.padre = ciudadActual
                        cola.append(vecino1)
            else: 
                return ciudadActual#print('Encontrado: '+ciudadActual.name +' Cosoto: '+ str(ciudadActual.costo))



    def desencolar():
        pass

    def imprimir_ruta(self):
        pass


def principal(graph):
    g = graph()
    for vert in ('Arad','Bucharest','Craiova','Dobreta','Eforie','Fagaras','Giurgiu','Hirsova','Iasi','Lugoj','Mehadia','Neamt','Oradea','Pitesti','Rimnicu Vilcea','Sibiu','Timisoara','Urziceni','Vaslui','Zerind'):
        g.add_ciudad(vert)

    g.add_conex('Arad','Sibiu',140)
    g.add_conex('Arad','Timisoara',118)
    g.add_conex('Arad','Zerind',75)

    g.add_conex('Bucharest','Fagaras',211)
    g.add_conex('Bucharest','Giurgiu',90)
    g.add_conex('Bucharest','Pitesti',101)
    g.add_conex('Bucharest','Urziceni',85)

    g.add_conex('Craiova','Dobreta',120)
    g.add_conex('Craiova','Pitesti',138)
    g.add_conex('Craiova','Rimnicu Vilcea',146)

    g.add_conex('Dobreta','Mehadia',75)
    
    g.add_conex('Eforie','Hirsova',86)
    
    g.add_conex('Fagaras','Sibiu',99)

    g.add_conex('Hirsova','Urziceni',98)
    
    g.add_conex('Iasi','Neamt',87)
    g.add_conex('Iasi','Vaslui',92)

    g.add_conex('Lugoj','Mehadia',70)
    g.add_conex('Lugoj','Timisoara',111)

    g.add_conex('Oradea','Sibiu',151)
    g.add_conex('Oradea','Zerind',71)

    g.add_conex('Pitesti','Rimnicu Vilcea',97)

    g.add_conex('Rimnicu Vilcea','Sibiu',80)
    g.add_conex('Urziceni','Vaslui',142)

    return g

G1=principal(Grafo)
#print(G1.costo_uniforme('Arad','Bucharest'))