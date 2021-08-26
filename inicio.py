emprestimo = str(input("Informe o valor do Empréstimo desejado: "))
emprestimoFinal = 0.0

if emprestimo.find(","):
    emprestimoFinal = float(emprestimo.replace(",", "."))
    print(emprestimoFinal)
else:
    emprestimoFinal = float(emprestimo)

if 2000 <= emprestimoFinal <= 10000:
    # juros composto
    active = True
    while active:
        try:
            escolha = input("Para valores entre 2000 e 10000 você poderá escolher entre 7 e 16 prestações: ")
            escolha = float(escolha)
            if not 7 <= escolha <= 16:
                raise ValueError("Valor incompatível!")
            else:
                parcelas = escolha
                break
        except ValueError as e:
            print("!erro!", e)
    calc = emprestimoFinal * ((1 + 0.015) ** escolha)
    calc = round(calc, 2)

    juros = ((1 + 0.015) ** escolha)
    juros = round(juros, 2)
    emprestimoParcela = emprestimoFinal/parcelas
    emprestimoParcela = round(emprestimoParcela, 2)
    jurosParcelaFinal = calc / parcelas
    jurosParcelaFinal = jurosParcelaFinal + emprestimoParcela
    jurosParcelaFinal = round(jurosParcelaFinal, 2)
    valorFinal = emprestimoFinal + calc
    valorFinal = round(valorFinal, 2)

    print(f"Você pagará {parcelas} x de R$ {emprestimoParcela} mais juros composto de {juros}% ao mês resultando em uma adicional de R$ {calc}.")
    print(f"O valor final a pagar é de R$ {valorFinal}. Cada parcela com juros fica no valor de R$ {jurosParcelaFinal}")
elif 250 <= emprestimoFinal <= 2000:
    # juros simples
    active = True
    while active:
        try:
            escolha = input("Para valores entre 250 e 2000 você poderá escolher entre 3 e 6 prestações: ")
            escolha = float(escolha)
            if not 3 <= escolha <= 6:
                raise ValueError("Valor incompatível!")
            else:
                parcelas = escolha
                break
        except ValueError as e:
            print("!erro!", e)
    calc = emprestimoFinal * 0.12 * escolha
    calc = round(calc, 2)
    emprestimoParcela = emprestimoFinal/parcelas
    emprestimoParcela = round(emprestimoParcela, 2)
    jurosParcelaFinal2 = calc / parcelas
    jurosParcelaFinal2 = jurosParcelaFinal2 + emprestimoParcela
    jurosParcelaFinal2 = round(jurosParcelaFinal2, 2)
    valorFinal = emprestimoFinal + calc
    valorFinal = round(valorFinal, 2)

    print(f"Você pagará {parcelas} x de R$ {emprestimoParcela} mais juros simples de 12% resultando em um adicional de R$ {calc}.")
    print(f"O valor final total é de R$ {valorFinal}. O valor com juros de cada parcela fica: R$ {jurosParcelaFinal2}")
else:
    active = True
    while active:
        try:
            print(f"O valor {emprestimoFinal} não pode ser contratado!")
            break
        except ValueError as e:
            print("!erro!", e)
