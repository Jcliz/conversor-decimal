def converter_binario(valor):
    numero = bin(valor)[2:]
    print(numero)


def converter_octal(valor):
    numero = oct(valor)[2:]
    print(numero)


def converter_hexadecimal(valor):
    numero = hex(valor)[2:].upper()
    print(numero)
