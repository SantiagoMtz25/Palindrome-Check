# Ozner Leyva Mariscal A01742377
# Carolina González Leal A01284948
# Erick Siller Ojeda A01382929
# Valeria Enríquez Limón A00832782
# Santiago Martínez Vallejo A00571878

# Complejidad de tiempo: O(m)
def buildPrefixTable(pattern):
    m = len(pattern)
    prefixTable = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefixTable[i] = length
            i += 1
        else:
            if length != 0:
                length = prefixTable[length - 1]
            else:
                prefixTable[i] = 0
                i += 1

    return prefixTable

# Complejidad de tiempo: O(n + m)
def kmp(filenameText, filenamePattern):
    text = ""
    pattern = ""

    with open(filenameText, 'r') as fileText:
        text = fileText.read().replace('\n', '')

    with open(filenamePattern, 'r') as filePattern:
        pattern = filePattern.read().replace('\n', '')

    n = len(text)
    m = len(pattern)

    prefixTable = buildPrefixTable(pattern)

    i = 0
    j = 0
    indices = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                indices.append(i - m)
                j = prefixTable[j - 1]
        else:
            if j != 0:
                j = prefixTable[j - 1]
            else:
                i += 1

    if indices:
        indicesStr = " ".join(map(str, indices))
        print("true", indicesStr)
    else:
        print("false")

# Complejidad de tiempo: O(n)
def manacherPalindrome(fileName):
    text = ''
    with open(fileName, 'r') as fileText:
        text = fileText.read().replace('\n', '')
      
    # Transformación del string
    transformedString = "#".join("^{}$".format(text))

    # Arreglo de palíndromos
    p = [0] * len(transformedString)
    center = right = 0
    maxLength = centerIndex = 0

    for i in range(1, len(transformedString) - 1):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])

        # Expansión alrededor del centro i
        while transformedString[i + 1 + p[i]] == transformedString[i - 1 - p[i]]:
            p[i] += 1

        # Actualización del palíndromo conocido más largo
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Actualización del palíndromo más largo
        if p[i] > maxLength:
            maxLength = p[i]
            centerIndex = i

    start = (centerIndex - 1 - maxLength) // 2
    end = start + maxLength
    return f"{start} {end}"

# Complejidad de tiempo: O(n*m)
def longestCommonSubstring(file1, file2):
    # Leer el contenido de los archivos
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()
      

    # Crear una matriz para almacenar las longitudes de las subcadenas comunes
    matrix = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    
    # Variables para almacenar la posición de la subcadena común más larga
    max_length = 0
    max_length_pos = 0
    
    # Llenar la matriz y actualizar la posición de la subcadena común más larga
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    max_length_pos = i
    
    # Calcular la posición inicial y final de la subcadena común más larga
    start_pos = max_length_pos - max_length
    end_pos = max_length_pos - 1

    print( start_pos, end_pos+1)

# parte 1
print('parte 1')
kmp("transmission1.txt", "mcode1.txt")
kmp("transmission1.txt", "mcode2.txt")
kmp("transmission1.txt", "mcode3.txt")
kmp("transmission2.txt", "mcode1.txt")
kmp("transmission2.txt", "mcode2.txt")
kmp("transmission2.txt", "mcode3.txt")

# parte 2
print('parte 2: ')
print(manacherPalindrome('transmission1.txt'))
print(manacherPalindrome('transmission2.txt'))

# parte 3
print('parte 3: ')
longestCommonSubstring('mcode2.txt','mcode3.txt')
      