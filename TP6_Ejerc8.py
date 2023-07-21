def main ():
    dividendo=int(input("Ingrese el dividendo de la operación: "))
    divisor=int(input("Ingrese el divisor de la operación: "))

#apartir de aqui comienza el if

    if divisor==0:
        print("No se puede dividir por 0!")

#apartir de aqui comienza el else
    else:
        resultado=dividendo/divisor
        print("El resultado de la operacion dividir es",resultado)
    print("Saludos")
    
if __name__=="__main__":
     main()
