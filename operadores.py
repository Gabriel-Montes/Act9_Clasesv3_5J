print("Gabriel Montes_Num de control:22308051281276")
print("--OPERADORES--")

# Clase
class ope:
    #Funciones
    def sum(self,g,m):
        ma=g+m
        print(f"La suma de {g} + {m} es: {ma}")
    def res(self,g,m):
        rres=g-m
        print(f"La resta de {g} - {m} es: {rres}")
    def mul(self,g,m):
        rmu=g*m
        print(f"La multiplicacion de {g} * {m} es: {rmu}")
    def div(self,g,m):
        rdi=g/m
        print(f"La division de {g} / {m} es: {rdi}")
    def mod(self,g,m):
        rmo=g%m
        print(f"El modulo de {g} % {m} es: {rmo}")
    def exp(self,g,m):
        rex=g**m
        print(f"El exponente de {g} ** {m} es: {rex}")
    def coc(self,g,m):
        rco=g//m
        print(f"El cociente de {g} // {m} es: {rco}")

#Objeto
opemon=ope()

# Uso de objeto
print('-Funcion Suma')
opemon.sum(12,5)
print('-Funcion Resta')
opemon.res(15,5)
print('-Funcion Multiplicacion')
opemon.mul(4,3)
print('-Funcion Division')
opemon.div(50,5)
print('-Funcion Modulo')
opemon.mod(45,5)
print('-Funcion Exponente')
opemon.exp(2,3)
print('-Funcion Cociente')
opemon.coc(28,4)

