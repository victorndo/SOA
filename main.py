print(  " ---------------------------------------------------------------------\n"
        "|       Bem vindo ao Algoritmo de Substituicao de Paginas.            |\n"
        "|  Esse algoritmo foi baseado no LRU e tem como funcao principal      |\n"
        "| contar as faltas de paginas na alocacao do enderecamento da memoria |\n"
        " ---------------------------------------------------------------------\n"
        "|         Esse software ira permitir duas opcoes de Paginacao         |\n"
        "|   1) O usuario ira criar seu proprio endereco e fazer o seu teste   |\n"
        "|   2) Um endereco pre-definido e com um valor fixo                   |\n"
        " ---------------------------------------------------------------------")
while True:
    try:
        opcaoEscolhida = int(input('Digite a opcao desejada: '))
        if not 1 == opcaoEscolhida and not opcaoEscolhida == 2:
            raise ValueError(" - Por favor, digite uma opcao valida")
    except ValueError as e:
        print("Valor invalido", e)
    #-----------------------------------------OPCAO 1 ---------------------------------------#       
    if opcaoEscolhida == 1:
        print(" ---------------------------------------------------------------------\n"
            "|                              OPCAO 1                                |\n"
            "|     Para iniciarmos, e necessario criar o endereco de memoria       |\n"
            "|    --->   (A quantidade minima de endereco permitido e 4)   <----   |\n"
            " ---------------------------------------------------------------------")
        endereco=[]
        while True:
            try:
                enderecoDigitado = int(input('Digite o tamanho do endereco a ser testado: '))
                if not 4 <= enderecoDigitado:
                    raise ValueError(" - Por favor, digite um numero de endereco maior que 3")
            except ValueError as e:
                print('Valor invalido', e)
            else: 
                for i in range(enderecoDigitado):
                    while True:
                        try:
                            alocacaoEndereco = int(input('Digite a posicao ('+str(i+1)+') do endereco: '))
                            if not 0 <= alocacaoEndereco <= 9:
                                raise ValueError(" - Por favor, digite um valor entre (0 e 9)")
                        except ValueError as e:
                            print('Valor invalido', e)
                        else:  
                            endereco.append(alocacaoEndereco) 
                            break       
                print('O endereco a ser testado e: '+str(endereco))
                valorTeste = 9010101010
                listaLru=[valorTeste,valorTeste,valorTeste]
                quantidadeFaltas=0
                quantidadeHit=0
                for n in range (enderecoDigitado):
                    print("Pagina acessada: " + str(endereco[n]))
                    if endereco[n] != listaLru[0] and endereco[n] != listaLru[1] and endereco[n] != listaLru[2]:
                        if listaLru[0] == valorTeste:
                            listaLru[0] = endereco[n]  
                        elif listaLru[1] == valorTeste:
                            listaLru[1] = endereco[n]
                        elif listaLru[2] == valorTeste:
                            listaLru[2] = endereco[n]
                        elif listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] != valorTeste:
                            listaLru[0] = listaLru[1]
                            listaLru[1] = listaLru[2]
                            listaLru[2] = endereco[n]
                        print("Houve falta de pagina: "+ str(endereco[n]))
                        print("Contem as seguintes paginas agora: ")   
                        for j in range (3):
                            if listaLru[j] != valorTeste:
                                print("------> " + str(listaLru[j]))
                            else:
                                print("------> ")
                        quantidadeFaltas = quantidadeFaltas+1
                    elif endereco[n] == listaLru[0] or endereco[n] == listaLru[1] or endereco[n] == listaLru[2]:
                        print("Nao houve falta de pagina: " + str(endereco[n]))            
                        if listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] != valorTeste:
                            if endereco[n] == listaLru[0]:
                                listaLru[0] = listaLru[1]
                                listaLru[1] = listaLru[2]
                                listaLru[2] = endereco[n]
                            elif endereco[n] == listaLru[1]:
                                listaLru[1] = listaLru[2]
                                listaLru[2] = endereco[n]
                        elif listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] == valorTeste:       
                            if endereco[n] == listaLru[0]:
                                listaLru[0] = listaLru[1]
                                listaLru[1] = endereco[n]
                        print("Houve atualizacoes de paginas: ") 
                        for j in range (3):
                            if listaLru[j] != valorTeste:
                                print("------> " + str(listaLru[j]))
                            else:
                                print("------> ") 
                        quantidadeHit = quantidadeHit+1
                print("----------------------------------------")                       
                print(" A quantidade total de faltas foi: " + str(quantidadeFaltas))
                print(" A quantidade total de Hit foi: " + str(quantidadeHit))
                print("----------------------------------------")
                break
        break
    # ----------------------------------------- OPCAO 2 ------------------------------------ #
    if opcaoEscolhida == 2:  
        print(" ---------------------------------------------------------------------\n"
            "|                              OPCAO 2                                |\n"
            "|         Nessa opcao, a execucao e feita de forma automatica         |\n"
            "|  O endereco criado para o teste e: [2,2,9,8,9,2,5,3,5,3,5,3,8,9,2]} |\n"
            " ---------------------------------------------------------------------")
        valorTeste = 9010101010
        endereco=[2,2,9,8,9,2,5,3,5,3,5,3,8,9,2]
        listaLru=[valorTeste,valorTeste,valorTeste]
        quantidadeFaltas=0
        quantidadeHit=0
        for n in range (15):
            print("ENDERECO DA PAGINA A SER ACESSADA: " + str(endereco[n]))
            if endereco[n] != listaLru[0] and endereco[n] != listaLru[1] and endereco[n] != listaLru[2]:
                if listaLru[0] == valorTeste:
                    listaLru[0] = endereco[n]  
                elif listaLru[1] == valorTeste:
                    listaLru[1] = endereco[n]
                elif listaLru[2] == valorTeste:
                    listaLru[2] = endereco[n]
                elif listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] != valorTeste:
                    listaLru[0] = listaLru[1]
                    listaLru[1] = listaLru[2]
                    listaLru[2] = endereco[n]
                print("Houve falta de pagina: "+ str(endereco[n]))
                print("Contem as seguintes paginas agora: ")   
                for j in range (3):
                    if listaLru[j] != valorTeste:
                        print("------> " + str(listaLru[j]))
                    else:
                        print("------> ")
                quantidadeFaltas = quantidadeFaltas+1
            elif endereco[n] == listaLru[0] or endereco[n] == listaLru[1] or endereco[n] == listaLru[2]:
                print("Nao houve falta de pagina: " + str(endereco[n]))            
                if listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] != valorTeste:
                    if endereco[n] == listaLru[0]:
                        listaLru[0] = listaLru[1]
                        listaLru[1] = listaLru[2]
                        listaLru[2] = endereco[n]
                    elif endereco[n] == listaLru[1]:
                        listaLru[1] = listaLru[2]
                        listaLru[2] = endereco[n]
                elif listaLru[0] != valorTeste and listaLru[1] != valorTeste and listaLru[2] == valorTeste:       
                    if endereco[n] == listaLru[0]:
                        listaLru[0] = listaLru[1]
                        listaLru[1] = endereco[n]
                print("Foram feitas as seguintes atualizacoes de paginas: ") 
                for j in range (3):
                    if listaLru[j] != valorTeste:
                        print("------> " + str(listaLru[j]))
                    else:
                        print("------> ") 
                quantidadeHit = quantidadeHit+1                   
        print("----------------------------------------")                       
        print(" A quantidade total de faltas foi: " + str(quantidadeFaltas))
        print(" A quantidade total de Hit foi: " + str(quantidadeHit))
        print("----------------------------------------")   
        break