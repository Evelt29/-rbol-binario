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