
def porcentaje(cantidad, total):
    porc = 0 
    if total > 0:
        porc = round(cantidad/total *100, 2)
    return porc


text = input("Ingresar texto: ").lower()
list_words = []

j = 0
for i in range(len(text)):
    if text[i] == ' ' or text[i] == '.':
        list_words.append(text[j:i])
        j = i+1

n = len(list_words)

# 1 - Determinar la cantidad de palabras del texto.
print("Cantidad de palabras en el texto: %s\n" % n)

# 2 - Determinar el promedio de letras por palabra.
count = 0
for word in list_words:
    count += len(word)
print("Promedio de letras por palabra: %s\n" % round(count/n, 2))

# 3 - Determinar el promedio de vocales por palabra.
for word in list_words:
    vowels = 0
    consonants = 0
    numeric = 0
    for char in word:
        if 'a' <= char <= 'z':
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1
        else:
            numeric += 1
    n = consonants + vowels + numeric
    
    print("Promedio de vocales en la palabra '%s': %s" % (word, vowels*100./n))
print()

# 4 - Determinar el promedio de consonantes por palabra.

for word in list_words:
    vowels = 0
    consonants = 0
    numeric
    for char in word:
        if 'a' <= char <= 'z':
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1
        elif '0' <= char <= '9':
            numeric += 1

    n = consonants + vowels + numeric
    print("Promedio de consonantes en la palabra '%s': %s" % (word, consonants*100./n))
print()
# 5 - Determinar la cantidad de palabras que incluyeron alguna letra e.

count = 0
for word in list_words:
    if "e" in word:
        count += 1

print("Cantidad de palabras con letra 'e': %s\n" % count)

# 6 - Determinar el porcentaje de palabras que incluyeron alguna consonante.

def exist_consonant(word):
    for char in word:
        if 'a' <= char <= 'z' and char not in "aeiou":
            return True
    return False

count = 0
for word in list_words:
    if exist_consonant(word):
        count += 1

n = len(list_words)
print("Porcentaje de palabras con alguna consonante: %s\n" % porcentaje(count, n))

# 7 - Determinar la cantidad de palabras que tuvieron exactamente 3 vocales.

def count_vowels(word):
    countv = 0
    for char in word:
        if 'a' <= char <= 'z':
            countv += 1
    return countv

count = 0
for word in list_words:
    if count_vowels(word) == 3:
        count += 1

print("Cantidad de palabras con exactamente 3 vocales: %s\n" % count)

# 8 - Determinar el porcentaje de palabras que tuvieron algún dígito ('0' al '9').

def exist_09(word):
    for char in word:
        if '0' <= char <= '9':
            return True
    return False

count = 0
for word in list_words:
    if exist_09(word):
        count += 1

print("Porcentaje de palabras con al menos un digito numerico: %s\n" % porcentaje(count, n))

# 9 - Determinar la cantidad de palabras que tuvieron más de 3 caracteres.

count = 0
for word in list_words:
    if len(word) >= 3:
        count += 1

print("Cantidad de palabras con mas de 3 caracteres: %s\n" % count)

# 10- Determinar la cantidad total dígitos del texto.

