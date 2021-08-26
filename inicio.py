active = True
while active:
    try:
        emprestimo = str(input("\nInforme o valor do Empréstimo desejado ou digite S para sair: "))
        emprestimoFinal = 0.0
        if emprestimo == "S" or emprestimo == "s":
            print("Desligando!")
            break
        elif emprestimo.find(","):
            emprestimoFinal = float(emprestimo.replace(",", "."))
            print(emprestimoFinal)
        elif emprestimo.find("."):
            emprestimoFinal = float(emprestimo)
            print(emprestimoFinal)
        else:
            raise ValueError("Informação incorreta!")

        tax = str(input(f"Informe o valor dos juros: "))
        if not -100 < int(tax) <= 100:
            raise ValueError("Informe um valor inteiro! Reiniciando o programa!")
        else:
            tax = float(tax) / 100
            print(tax)

        tipo = str(input(f"Juros Simples ou Juros Composto [S ou C]: "))

        if emprestimoFinal <= 100:
            raise ValueError("Valor muito pequeno!")

        if tipo == "C" or tipo == "c":
            # juros composto
            active = True
            while active:
                try:
                    escolha = input("Para empréstimos com juros composto você poderá escolher entre 5 e 20 prestações: ")
                    escolha = int(escolha)
                    if not 5 <= escolha <= 20:
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
                calc = calc + (calc * tax)
                calc = round(calc, 2)
                totalParcelas = totalParcelas + calc
                print(f"No {cont}º mês você pagará o valor de R$ {calc}")
                i += 1

            valorFinalJuros = totalParcelas - emprestimoFinal
            valorFinalJuros = round(valorFinalJuros, 2)
            totalParcelas = round(totalParcelas, 2)

            print(f"Valor solicitado: R$ {emprestimoFinal}\nValor final total com juros composto: R$ {totalParcelas}\nValor total dos juros adicionado: R$ {valorFinalJuros}\n")
        
        elif tipo == "S" or tipo == "s":
            # juros simples
            active = True
            while active:
                try:
                    escolha = input("Para empréstimos a juros simples você poderá escolher entre 3 e 12 prestações: ")
                    escolha = int(escolha)
                    if not 3 <= escolha <= 12:
                        raise ValueError("Valor incompatível!")
                    else:
                        parcelas = float(escolha)
                        break
                except ValueError as e:
                    print("!erro!", e)
            calc = emprestimoFinal * tax * parcelas
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
    except ValueError as e:
        print("!erro!", e)
