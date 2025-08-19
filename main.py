def converter_binario(valor):
    return bin(valor)[2:]


def converter_octal(valor):
    return oct(valor)[2:]



def converter_hexadecimal(valor):
    return hex(valor)[2:].upper()

def __init__():
    numero = int(input("Digite um número decimal inteiro: "))
    print(f"\nSeu número: {numero}\n")
    print(f"Em binário: {converter_binario(numero)}\n")
    print(f"Em octal: {converter_octal(numero)}\n")
    print(f"Em hexadecimal: {converter_hexadecimal(numero)}\n")

__init__()