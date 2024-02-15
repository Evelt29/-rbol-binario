class nodo():
    def __init__(self,valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        pass
    def __str__(self):
        return f"valor: {self.valor}, izq: {self.izquierda}, der: {self.derecha}"
    
pass