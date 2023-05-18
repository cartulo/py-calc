# -*- coding: utf-8 -*-
import sys
try:
    A = float(input("Digite o primeiro número: "))
    B = float(input("Digite o segundo número: "))
    operacao = input("Digite uma operação (+ ou - ou * ou /) ")

    if operacao == "+":
        resultado = float(A) + float(B)
    elif operacao == "-":
        resultado = float(A) - float(B)
    elif operacao == "*":
        resultado = float(A) * float(B)
    elif operacao == "/":
        resultado = float(A) / float(B)
    else:
        print("================================================")
        print("Operação não existente!")
        sys.exit(1)

    if resultado:
        print("================================================")
        print("Resultado: {0}".format(resultado))
        print("================================================")
        input("Pressione qualquer tecla para sair.")

except (TypeError, NameError, SyntaxError, ValueError):
    print("================================================")
    print("Apenas números são aceitos")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

except ZeroDivisionError:
    print("================================================")
    print("Impossível dividir por zero.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")