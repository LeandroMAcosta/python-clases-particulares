# texto = input().lower()


# 1 - Determinar la cantidad de palabras del texto.
# cantidad_palabras = 0

# count = 0
# for car in texto:
#     if car == ' ' or car == '.':
#         count += 1
    
#     if car != ' ' and car != '.' :
#         cantidad_letras += 1

# print(car)

# def pingo(cantidad, total):
#     return cantidad/total * 100

# cantidad_p_cn = 0
# cantidad_palabras = 0
# flag_cn = False

# for car in texto:
#     if car == ' ' or car == '.':
#         cantidad_palabras += 1
#     if '0' <= car <= '9' and flag_cn == False:
#         cantidad_p_cn += 1
#         flag_cn = True 

# print( pingo(cantidad_p_cn, cantidad_palabras))


#  Parcial

# contador_pares = 0
# cantidad_letras_por_palabra = 0
# primer_palabra = True
# cantidad_pp = 0
# # la puta madre. -> ["la", "puta", "madre"]
# contador_digitos_primer_palabra = 0

# resultado_punto2 = 0

# for car in texto:
#     if car == ' ' or car == '.':    #llege al final de una palabra
#         if cantidad_letras_por_palabra % 2 == 0:
#             contador_pares += 1
        
#         if primer_palabra:
#             contador_digitos_primer_palabra = cantidad_letras_por_palabra
#         elif contador_digitos_primer_palabra == cantidad_letras_por_palabra:
#             resultado_punto2 += 1

#         cantidad_letras_por_palabra = 0
#         primer_palabra = False

#     else:                                       # Cuando no es un espacio o punto
#         cantidad_letras_por_palabra += 1

# print(resultado_punto2)

text = input("Ingresar texto: ").lower()
list_words = []

j = 0
# lista vacia con palabras.

for i in range(len(text)):
    if text[i] == ' ' or text[i] == '.':
        list_words.append(text[j:i])        
        j = i + 1                           # posicion de la nueva palabra

punto1 = 0
punto2 = 0

contador_de_c = 0   #pprimera mitad
contador_de_s = 0   # segunda mitad
contador_de_palabras_que_empiezan_con_p = 0
sumador_p = 0

for palabra in list_words:
    # Punto 1
    if len(palabra) % 2 == 0:
        punto1 += 1

    # punto 2:
    
    if len(list_words[0]) == len(palabra):
        punto2 += 1

    # Punto 3
    n = len(palabra)
    punto_medio = int(n/2)
    if 'c' in palabra[0:punto_medio]:
        contador_de_c += 1
    if 's' in palabra[punto_medio:]:
        contador_de_s += 1
    
    # Punto 4
    if palabra[0] == 'p':
        contador_de_palabras_que_empiezan_con_p += 1
        sumador_p += len(palabra)
    
print(punto1)
print(punto2-1)

print(contador_de_c)
print(contador_de_s)
print(sumador_p/contador_de_palabras_que_empiezan_con_p)