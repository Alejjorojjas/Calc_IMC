

print('Calculadora de imc para adolecentes y adultos')
res = "s"

while res == "s" :
    edad = int(input('Ingrese su edad: '))
    print("Ingrese un Peso en kilogramos: ")
    peso = float(input ())
    peso = float(peso)
    #print(type(peso))
    print("Ingrese un Altura en metros: ")
    altura = float(input())
    
    imc = (peso / (altura*altura))
    
    print("Su indice de masa corporal es: " + str(imc))

    if edad >= 35:

        if imc <= 18.4 :
            print("Subpesado o Bajo de peso.")
        if 18.5 <= imc <= 24.9 :
            print("Peso Normal.")
        if 25 <= imc <= 29.9 :
            print("Está en Sobrepeso.")
        if 30 <= imc <= 34.9 :
            print("Obesidad grado 1.")
        if 35 <= imc <= 39.9 :
            print("Obesidad grado 2.")
        if imc > 34.9 :
            print("Clínicamente obesos.")

    if edad < 35:

        if imc <= 18.4 :
            print("Subpesado o Bajo de peso.")
        if 18.5 <= imc <= 24.9 :
            print("Peso Normal.")
        if 25 <= imc <= 29.9 :
            print("Está en Sobrepeso.")
        if 30 <= imc <= 34.9 :
            print("Obesidad grado 1.")
        if 35 <= imc <= 39.9 :
            print("Obesidad grado 2.")
        if imc > 34.9 :
            print("Obesidad grado 3.")

    res  =  input(" Desea hacer otro calculo de imc? \n Escriba s para si o cualquier tecla para Salir \n")




