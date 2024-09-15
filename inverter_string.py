def inverte_string(texto):
    string_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]
    return string_invertida

entrada = input("Digite uma string: ")
resultado = inverte_string(entrada)
print("String invertida:", resultado)
