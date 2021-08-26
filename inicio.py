emprestimo = str(input("Informe o valor do Empréstimo desejado: "))
emprestimoFinal = 0.0

if emprestimo.find(","):
    emprestimoFinal = float(emprestimo.replace(",", "."))
    print(emprestimoFinal)
else:
    emprestimoFinal = float(emprestimo)
    print(emprestimoFinal)

if 2000 <= emprestimoFinal <= 10000:
    # juros composto
    active = True
    while active:
        try:
            escolha = input("Para valores entre 2000 e 10000 você poderá escolher entre 7 e 16 prestações: ")
            escolha = int(escolha)
            if not 7 <= escolha <= 16:
                raise ValueError("Valor incompatível!")
            else:
                parcelas = float(escolha)
                break
        except ValueError as e:
            print("!erro!", e)
    # calc = emprestimoFinal * ((1 + 0.015) ** escolha)
    # calc = round(calc, 2)
    
    emprestimoParcela = emprestimoFinal/parcelas
    emprestimoParcela = round(emprestimoParcela, 2)
    totalParcelas = 0.0
    calc = emprestimoParcela
    print(f"Você solicitou {escolha} parcelas!")
    for i in range(escolha):
        cont = i + 1
        calc = calc + (calc * 0.015)
        calc = round(calc, 2)
        totalParcelas = totalParcelas + calc
        print(f"No {cont}º mês você pagará o valor de R$ {calc}")
        i += 1

    valorFinalJuros = totalParcelas - emprestimoFinal
    valorFinalJuros = round(valorFinalJuros, 2)
    totalParcelas = round(totalParcelas, 2)

    print(f"Valor solicitado: R$ {emprestimoFinal}\nValor final total com juros composto: R$ {totalParcelas}\nValor total dos juros adicionado: R$ {valorFinalJuros}\n")
 
elif 250 <= emprestimoFinal <= 2000:
    # juros simples
    active = True
    while active:
        try:
            escolha = input("Para valores entre 250 e 2000 você poderá escolher entre 3 e 6 prestações: ")
            escolha = int(escolha)
            if not 3 <= escolha <= 6:
                raise ValueError("Valor incompatível!")
            else:
                parcelas = float(escolha)
                break
        except ValueError as e:
            print("!erro!", e)
    calc = emprestimoFinal * 0.12 * parcelas
    calc = round(calc, 2)
    valorFinalJuros = emprestimoFinal + calc
    valorFinalJuros = round(valorFinalJuros, 2)

    valorParcela = (emprestimoFinal / parcelas) + (calc / parcelas)
    valorParcela = round(valorParcela, 2)
    
    print(f"Valor solicitado: R$ {emprestimoFinal}\nValor final total com juros simples: R$ {valorFinalJuros}\nValor total dos juros adicionado: R$ {calc}\nValor de cada uma das {escolha} parcelas: R$ {valorParcela}")

else:
    active = True
    while active:
        try:
            print(f"O valor {emprestimoFinal} não pode ser contratado!")
            break
        except ValueError as e:
            print("!erro!", e)
