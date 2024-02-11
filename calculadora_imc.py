#Pedimos el nombre y lo validamos
nombre_valido = False
while nombre_valido == False:
    try:
        nombre = input('Por favor ingrese su nombre: ')             #pedimos el nombre 
        if nombre.strip() == '':                                    #validamos  que el campo no este vacio
            print('Dato nulo. Ingresa un nombre válido.')
        elif any(char.isdigit() for char in nombre):                #validamos que el campo no incluya ningun digito
            print('El nombre no puede contener dígitos.Por favor ingresa un nombre válido.')
        else:
            nombre = nombre.capitalize()                            #transformamos la primera letra en mayusculas y las demas en minisculas para que se vea mejor
            nombre_valido = True                                    #validamos el nombre, si no está vacío y no contiene ningun digitos establecemos en true para salir del bucle
    except ValueError:
        print('Por favor, ingresa un nombre válido.')


#Pedimos el apellido paterno y lo validamos
apellidoP_valido = False
while apellidoP_valido == False:
    try:
        apellido_paterno = input('Por favor ingrese su apellido Paterno: ')
        if apellido_paterno.strip() == '':
            print('Dato nulo. Ingresa un apellido válido.')
        elif any(char.isdigit() for char in apellido_paterno):
            print('El apellido no puede contener dígitos. Ingresa un apellido válido.')
        else:
            apellido_paterno = apellido_paterno.capitalize()
            apellidoP_valido = True
    except ValueError:
        print('Por favor, ingresa un apellido válido.')

#Pedimos el apellido materno y lo validamos
apellidoM_valido = False
while apellidoM_valido == False:
    try:
        apellido_materno = input('Apellido Materno: ')
        if apellido_materno.strip() == '':
            print('Dato nulo. Ingresa un apellido válido.')
        elif any(char.isdigit() for char in apellido_materno):
            print('El apellido no puede contener dígitos. Ingresa un apellido válido.')
        else:
            apellido_materno = apellido_materno.capitalize()
            apellidoM_valido = True
    except ValueError:
        print('Por favor, ingresa un apellido válido.')

#Pedimos la edad y lo validamos
edad_validado = False
while edad_validado == False:
    try:
        edad = input('Por favor ingrese su edad: ')
        if  edad is not None:                                       #se verifica si no esta vacio
            edad = float(edad)                                      #convertimos a float para checar que introdujo un digito
        if  edad > 0:                                               #Verificar si la edad no es cero
            edad_validado = True                                    #validamos que este correcto, si es asi se sale del bucle
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')

#Pedimos la estatura y lo validamos
estatura_validado = False
while estatura_validado == False:
    try:
        estatura = input('Por favor ingrese su estatura en metros: ')
        if  estatura is not None:
            estatura = float(estatura)
        if estatura > 0:                                   
            estatura_validado = True
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')   

#Pedimos el peso y lo validamos
peso_validado = False
while peso_validado == False:
    try:
        peso = input('Por favor ingrese su peso en kilogramos: ')
        if  peso is not None:
            peso = float(peso)
        if  peso > 0:  
            peso_validado = True
        else:
            print('Ingresa un dato no nulo')
    except ValueError:
        print('Por favor, ingresa un valor númerico')      

#calculamos el indice de masa corporal con la formula
imc = peso / estatura**2
imc_resultado = "{:.2f}".format(imc)                                #formateamos el resultado para que solo nos de dos digitos

#comparamos el resultado con la tabla para ver si es saludable y lo guardamos en un variable
categoria_imc = ""
if imc >= 0 and imc <= 15.99:
    categoria_imc = "Delgadez severa"
elif imc >= 16.00 and imc <= 16.99:
    categoria_imc = "Delgadez moderada"
elif imc >= 17.00 and imc <= 18.49:
    categoria_imc = "Delgadez leve"
elif imc >= 18.50 and imc <= 24.99:
    categoria_imc = "tu peso Normal"
elif imc >= 25.00 and imc <= 29.99:
    categoria_imc = "Sobrepeso"
elif imc >= 30.00 and imc <= 34.99:
    categoria_imc = "Obesidad leve"
elif imc >= 35.00 and imc <= 39.00:
    categoria_imc = "Obesidad media"
elif imc >= 40.00:
    categoria_imc = "Obesidad morbida"


#imprimimos los resultados de la persona
print("---------Datos----------")    
print("Nombre:", nombre)
print("Apellido Paterno:", apellido_paterno)
print("Apellido Materno:", apellido_materno)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "metros")
print("Tu índice de masa corporal es:", imc_resultado)
print("En base a tu índice de masa corporal tienes:", categoria_imc)