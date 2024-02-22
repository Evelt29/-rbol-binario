from Lib import *

inOrderArr=[]

nodo1 = nodo(1)
nodo2 = nodo(2)
nodo3 = nodo(3)
nodo4 = nodo(4)
nodo5 = nodo(5)
nodo6 = nodo(6)
nodo7 = nodo(7)


# LVR IN ORDER
linkHijo(nodo1,nodo2,nodo3)
linkHijo(nodo2,nodo4,nodo5)
linkHijo(nodo3,nodo6,nodo7)




LVR(nodo1,inOrderArr)
print("------IN ORDER ----------")
print( inOrderArr)

# LRV POST ORDER
postOrderArr=[]
LRV(nodo1,postOrderArr)
print("------POST ORDER ----------")
print(postOrderArr)

# VLF PRE ORDER 
preOrderArr=[]
VLF(nodo1,preOrderArr)
print("------PRE ORDER ----------")
print(preOrderArr)

#print(nodo1.getArbol())
#print(nodo2.getArbol())
print("-----------------------------------------------")
nodoRaiz = nodo(16)
nodo9 = nodo(5)
nodo10 = nodo(7)
nodo11 = nodo(12)
nodo12 = nodo(9)
nodo13 = nodo(20)
nodo14 = nodo(18)
nodo15 = nodo(3)
nodo16 = nodo(10)
nodo17 = nodo(14)
print("----------------------------------------------------")



arrNodos = [16,5,7,12,9,20,18,13,10,14]
nodoRaiz = None
for i in range (0,len(arrNodos),1):
    if i == 0:
        nodoRaiz = nodo(arrNodos[i])
    else:
        nodosOrdenados(nodoRaiz,nodo(arrNodos[i]))
    pass
     
printArbol(nodoRaiz)
    
    

