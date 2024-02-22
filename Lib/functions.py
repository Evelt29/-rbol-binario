def linkHijo(nodoPadre, nodoHijoIz=None, nodoHijoDer=None):
    if nodoHijoIz is not None:
        nodoPadre.izquierda = nodoHijoIz
    if nodoHijoDer is not None:
        nodoPadre.derecha = nodoHijoDer

def LVR(nodo, inOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        LVR(nodoPadre.izquierda,inOrderArr)    
        inOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.derecha,inOrderArr) 
        
        
        return inOrderArr
    

def LRV(nodo, postOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        LRV(nodoPadre.izquierda,postOrderArr)    
        LRV(nodoPadre.derecha,postOrderArr) 
        postOrderArr.append(nodoPadre.valor)
        
        return postOrderArr
    
def VLF(nodo, preOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        preOrderArr.append(nodoPadre.valor)
        VLF(nodoPadre.izquierda,preOrderArr)    
        VLF(nodoPadre.derecha,preOrderArr) 
        
        
        return preOrderArr
    
    
    #_______________________NODOS ORDENADOS_______________________
    
def nodosOrdenados(nodoPadre, newNodo):
    if newNodo.valor < nodoPadre.valor: #izquierda
        if nodoPadre.izquierda is None:  
            nodoPadre.izquierda = newNodo
        else:
            nodosOrdenados(nodoPadre.izquierda, newNodo)
                    
    if newNodo.valor > nodoPadre.valor: #izquierda
        if nodoPadre.derecha is None:  
            nodoPadre.derecha = newNodo
        else:
            nodosOrdenados(nodoPadre.derecha, newNodo)
