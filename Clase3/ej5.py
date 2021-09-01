#Funcion sin argumentos y que no regresa valor
def imprimir():
    print("Hola")

#Funciuon que recibe argunento y no regresa ningun valor
def funcion_imprimir_argumento(valor_a_imprimir):
    print(valor_a_imprimir)

#otro ejemplo de una función que no regresa valor pero recibe dos argumentos
def adicionar_dos_argumentos(a,b):
    print(a+b)


if __name__ == "__main__":
    # imprimir()
    # lista_valores_impimir = ["Soy el #",1,"por que voy en","UPIITA"]
    # for elemento in lista_valores_impimir:
    #     funcion_imprimir_argumento(elemento)

    #Primera llamada a la función
    # adicionar_dos_argumentos('Hola','mundo!!')

    # #Segunda llamada a la funcion
    # adicionar_dos_argumentos(1,2)

    # #Tercera llamada a la funcion
    # adicionar_dos_argumentos(1+2j,2+3j)

    # #Cuarta llamada a la funcion
    # adicionar_dos_argumentos([1,2,3],[4,5,6])

    #Funcion inusual, una que regresa valor y no recibe argumentos
    cuenta = 1
    def lleva_la_cuenta():
        global cuenta
        cuenta = cuenta + 1
    print(cuenta)
    lleva_la_cuenta()
    lleva_la_cuenta()
    lleva_la_cuenta()
    print(cuenta)