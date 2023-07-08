def main ():
    dividendo=int(input("Ingrese el dividendo de la operación: "))
    divisor=int(input("Ingrese el divisor de la operación: "))
    #solo prueba
    #hola mundo
    if divisor==0:
        print("No se puede dividir por 0!")
    else:
        resultado=dividendo/divisor
        print("El resultado de la operacion dividir es",resultado)
    print("Saludos")
    
if __name__=="__main__":
     main()
