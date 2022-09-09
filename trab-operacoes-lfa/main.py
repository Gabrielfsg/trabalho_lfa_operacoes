from AutomatoFD import AutomatoFD

if __name__ == '__main__':

    afd = AutomatoFD('ab')

    for i in range(1, 9):
        afd.criaEstado(i)
        afd.qtdEstados = i


    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(4, True)

    afd.criaTransicao(1, 5, 'a')
    afd.criaTransicao(2, 7, 'a')
    afd.criaTransicao(3, 5, 'a')
    afd.criaTransicao(4, 8, 'a')
    afd.criaTransicao(5, 1, 'a')
    afd.criaTransicao(6, 3, 'a')
    afd.criaTransicao(7, 1, 'a')
    afd.criaTransicao(8, 4, 'a')
    afd.criaTransicao(1, 2, 'b')
    afd.criaTransicao(2, 2, 'b')
    afd.criaTransicao(3, 4, 'b')
    afd.criaTransicao(4, 4, 'b')
    afd.criaTransicao(5, 6, 'b')
    afd.criaTransicao(6, 6, 'b')
    afd.criaTransicao(7, 8, 'b')
    afd.criaTransicao(8, 8, 'b')

    #afd.salvarArquivo("C:\\Users\\jr_jo\\Desktop","afdsalvo")


    print(afd)

    cadeia = 'abbabaabbbbbba'
    afd.limpaAfd()
    parada = afd.move(cadeia)
    if not afd.deuErro() and afd.estadoFinal(parada):
        print('Aceita cadeia "{}"'.format(cadeia))
    else:
        print('Rejeita cadeia "{}"'.format(cadeia))

    print("###COMPLEMENTO###")
    print(afd.guritimo_complemento())
    print("###")
