#Ejercicio 1
def digitos(numero_de_tarjeta: str) -> int:
    digitos = len(numero_de_tarjeta)
    return digitos

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str,tamaño_prefijo: int) -> int:
    prefijo = int(numero_de_tarjeta[:tamaño_prefijo])
    return prefijo

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    
    cant_digito = digitos(numero_de_tarjeta)
    if len(numero_de_tarjeta) < 4:
        return 'Invalid'
    prefijo = obtener_prefijo(numero_de_tarjeta, 4)
    
    if (prefijo <= 3499 and prefijo >= 3400) or (prefijo <= 3799 and prefijo >= 3700) :
        if cant_digito == 15:
            return 'American Express'
    if (prefijo <= 5599 and prefijo >= 5100):
        if cant_digito == 16:
            return 'Mastercard'
    if (prefijo <= 4999 and prefijo >= 4000):
        if cant_digito == 16 or cant_digito == 13:
            return 'Visa'
    if (prefijo <= 3699 and prefijo >= 3600) or (prefijo <= 3899 and prefijo >= 3800) or (prefijo <= 3059 and prefijo >= 3000):
        if cant_digito == 14:
            return 'Diners Club y Carte Blanche'
    if (prefijo == 6011):
        if cant_digito == 16:
            return 'Discover'
    if (prefijo == 2123 or prefijo == 1800):
        if cant_digito == 15:
            return 'JCB'
    if (prefijo <= 3999 and prefijo >= 3000):
        if cant_digito == 16:
            return 'JCB'
        
    return 'Invalid'
        

#Ejercicio 4
def digitos_impares(numero_de_tarjeta : str) -> list[int]:
    reversed_card = numero_de_tarjeta[::-1]
    lista_impares = []
    for x in range(len(numero_de_tarjeta)):
        if x % 2 == 0:
            lista_impares.append(int(reversed_card[x]))
    return lista_impares

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    reversed_card = numero_de_tarjeta[::-1]
    lista_pares = []
    for x in range(len(numero_de_tarjeta)):
        if x % 2 == 1:
            lista_pares.append(int(reversed_card[x]))
    return lista_pares

#Ejercicio 6
def sumar_digitos(lista_digitos : list[int]) -> int:
    str_digitos=""
    suma = 0
    for x in range(len(lista_digitos)):
        str_digitos+= str(lista_digitos[x])
    
    for x in range(len(str_digitos)):
        suma+= int(str_digitos[x])
        
    return suma

#Ejercicio 7
def luhn(numero_de_tarjeta :  str) -> bool:
    lista_digitos_pares= digitos_pares(numero_de_tarjeta)
    suma = 0
    
    for x in range(len(lista_digitos_pares)):
        lista_digitos_pares[x]*=2
        
    suma += sumar_digitos(lista_digitos_pares)
    lista_digitos_impares = digitos_impares(numero_de_tarjeta)
    suma += sumar_digitos(lista_digitos_impares)
    
    if suma % 10 == 0 : 
        return True
    else:
        return False

#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    Luhn = luhn(numero_de_tarjeta)
    Is_Valid_Card = tipo_tarjeta(numero_de_tarjeta)
    if  Luhn == True:  
        if Is_Valid_Card != "Invalid" :
            return True
        else:
            return False
    else:
        return False