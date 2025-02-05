def cesar (cadena, correlation):
    resultado = ""
    for letra in cadena:
        ordinal_char = ord(letra)
        converted_char = ordinal_char + correlation
        if (ordinal_char >= ord('A') and ordinal_char <= ord('Z')):
            
            if converted_char > ord('Z'):
                resultado += chr(ord('A') + converted_char - ord('Z')-1) #Lo que excedo del ordinal del caracter Z se lo agrego al ordinal del carácter A. Es decir, si me paso de Z, tengo que empezar por A sólo en lo que me haya pasado. Misma idea para las minúsculas. Resto de los caracteres no alfabéticos no se convierten.
            else:
                resultado += chr(converted_char)
        elif (ordinal_char >=ord('a') and ordinal_char <= ord('z')):
            if converted_char > ord('z'):
                resultado += chr(ord('a') + converted_char - ord('z')-1)
            else:
                resultado += chr(converted_char)
        else:
            resultado += letra
    return resultado

print(cesar('abcxyzABCxyz 123',2))
print(cesar('The',25))
print(cesar('The die is cast',25))