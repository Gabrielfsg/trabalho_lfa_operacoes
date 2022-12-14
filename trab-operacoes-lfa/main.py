from AutomatoFD import *

if __name__ == '__main__':

    afd = AutomatoFD('ab')

    #AFD Lista 1 Exercício 7 - nao contem bab e contem par de a
    for i in range(1, 9):
        afd.criaEstado(i)
        afd.qtdEstados = i

    afd.mudaEstadoInicial(1)
    afd.mudaEstadoFinal(1, True)
    afd.mudaEstadoFinal(2, True)
    afd.mudaEstadoFinal(3, True)

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
    afd.funcao = "nao contem bab e contem par de a"

    #print(afd.transicoes)

    #afd.salvarArquivo("AFDTeste")

    print(afd)

    cadeia = 'abbabaabbbbbba'
    afd.limpaAfd()
    parada = afd.move(cadeia)
    if not afd.deuErro() and afd.estadoFinal(parada):
        print('Aceita cadeia "{}"'.format(cadeia))
    else:
        print('Rejeita cadeia "{}"'.format(cadeia))

    print("###COMPLEMENTO###")
    afd.salvarArquivo('AFD_ANTES_DO_COMPLEMENTO')
    afd.complemento_automato().salvarArquivo('ComplementoAFD')
    print("###")

    # print("\n ###Multiplicação/Intersecção/União/Diferença###")
    #
    # afdM1 = AutomatoFD('ab');
    # afdM2 = AutomatoFD('ab');
    #
    # for i in range(1, 5):
    #     afdM1.criaEstado(i)
    #
    # for i in range(1, 3):
    #     afdM2.criaEstado(i)
    #
    # afdM1.criaTransicao(1, 2, 'b')
    # afdM1.criaTransicao(1, 1, 'a')
    # afdM1.criaTransicao(2, 2, 'b')
    # afdM1.criaTransicao(2, 3, 'a')
    # afdM1.criaTransicao(3, 4, 'b')
    # afdM1.criaTransicao(3, 1, 'a')
    # afdM1.criaTransicao(4, 4, 'a')
    # afdM1.criaTransicao(4, 4, 'b')
    #
    # afdM2.criaTransicao(1, 1, 'b')
    # afdM2.criaTransicao(1, 2, 'a')
    # afdM2.criaTransicao(2, 2, 'b')
    # afdM2.criaTransicao(2, 1, 'a')
    #
    # afdM1.mudaEstadoInicial(1)
    # afdM2.mudaEstadoInicial(1)
    #
    # afdM2.mudaEstadoFinal(1, True)
    # afdM1.mudaEstadoFinal(1, True)
    # afdM1.mudaEstadoFinal(2, True)
    # afdM1.mudaEstadoFinal(3, True)
    #
    # print(afdM1)
    # print(afdM2)
    # afdM1.salvarArquivo('afdM1')
    # afdM2.salvarArquivo('afdM2')
    #
    # automato_mult, estados = afdM1.multiplicacao_automato(afdM2)
    # print("AFDs multiplicados")
    # print(automato_mult)
    # automato_mult.salvarArquivo('AFDM1M2')
    # print(estados)
    # print("AFDs INTERSECÇÃO")
    # afdIntersec = afdM1.intersecao_automato(afdM2, automato_mult, estados)
    # print(afdIntersec)
    # afdIntersec.salvarArquivo('AFDM1M2_INTER')
    # print("AFDs UNIÃO")
    # afdUni = afdM1.uniao_automato(afdM2, automato_mult, estados)
    # print(afdUni)
    # afdUni.salvarArquivo('AFDM1M2_UNIAO')
    # print("AFDs DIFERENÇA")
    # afdDif = afdM1.diferenca_automato(afdM2, automato_mult, estados)
    # afdDif.salvarArquivo('AFDM1M2_DIFERENCA')


    #print("\n ###MINIMIZAÇÃO AUTOMATOS###")

    # print(afd)
    # afd.automatoMinimo()

    # afd2 = importarAFD("Automatos_Para_Teste/AFDTeste.jff")
    # print(afd2)
    # afd2.automatoMinimo()
    # print("\nAutomato depois de minimizar")
    # print(afd2)
    # afd2.salvarArquivo("AFDTeste2SalvoMin")

    # afdPre_Sux = importarAFD('Automatos_Para_Teste/prefixo_ab-sufixo_ab.jff')
    # print(afdPre_Sux)
    # afdPre_Sux.automatoMinimo()
    # afdPre_Sux.salvarArquivo("teste")

    # afdDesconexo = importarAFD('Automatos_Para_Teste/AFDDESCONEXO.jff')
    # print(afdDesconexo)
    # afdDesconexo.automatoMinimo()
    # afdDesconexo.salvarArquivo('teste')

    # afdP1 = importarAFD('Automatos_Para_Teste/AFDPROVA1.jff')
    # print(afdP1)
    # afdP1.automatoMinimo()
    # afdP1.salvarArquivo('afdprova1min')

    # print("\n ###EQUIVALENCIA AUTOMATOS###")
    #
    # afdM3 = AutomatoFD('ab');
    # afdM4 = AutomatoFD('ab');
    #
    # for i in range(1, 4):
    #     afdM3.criaEstado(i)
    #
    # for i in range(1, 3):
    #     afdM4.criaEstado(i)
    #
    # afdM3.criaTransicao(1, 2, 'b')
    # afdM3.criaTransicao(1, 3, 'a')
    # afdM3.criaTransicao(2, 2, 'b')
    # afdM3.criaTransicao(2, 1, 'a')
    # afdM3.criaTransicao(3, 2, 'b')
    # afdM3.criaTransicao(3, 3, 'a')

    # afdM3.criaTransicao(1, 1, 'b')
    # afdM3.criaTransicao(1, 2, 'a')
    # afdM3.criaTransicao(2, 2, 'b')
    # afdM3.criaTransicao(2, 1, 'a')

    # afdM4.criaTransicao(1, 1, 'b')
    # afdM4.criaTransicao(1, 2, 'a')
    # afdM4.criaTransicao(2, 2, 'b')
    # afdM4.criaTransicao(2, 1, 'a')
    #
    # afdM3.mudaEstadoInicial(1)
    # afdM4.mudaEstadoInicial(1)
    #
    # afdM3.mudaEstadoFinal(2, True)
    # afdM4.mudaEstadoFinal(2, True)
    #
    # print(afdM3)
    # print(afdM4)
    #
    # print(afdM3.automatoEquivalentes(afdM4))

    #afdM3.salvarArquivo("AFDM3")
    #afdM4.salvarArquivo("AFDM4")








  
