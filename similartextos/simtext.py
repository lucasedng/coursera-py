 # coding=utf8
import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#################################################################


def soma_qtd_char(lista_palavras):
    # retorna a quantidade de caracteres

    soma = 0
    for palavra in lista_palavras:
        soma += len(palavra)

    return soma


def tam_medio_sent(lista_sentencas):
    # retorna o tamanho médio das sentencas

    soma = 0
    for sentenca in lista_sentencas:
        soma += soma_qtd_char(sentenca)

    return soma/len(lista_sentencas)


def tam_medio_frase(lista_frases):
    # retorna o tamanho médio das frases

    new_list = []
    for frase in lista_frases:
        new_list.append(re.sub(r'[?!,.:;-+]', '', frase))

    soma = 0
    for frase in new_list:
        soma += len(frase)

    return soma/len(new_list)


def compara_assinatura(as_a, as_b):
    # Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.

    grau = 0
    for parametro in range(len(as_a)):
        grau += abs(as_a[parametro]-as_b[parametro])

    return grau/len(as_a)


def num_frases(lista_sentencas):
    # contabiliza o número total de frases levando em consideracao todas as sentencas

    lista_frases = []
    for sentenca in lista_sentencas:
        lista_frases.append(separa_frases(sentenca))

    counter = 0
    for sub_listas in lista_frases:
        counter += len(sub_listas)

    return counter


def calcula_assinatura(texto):
    # Essa funcao recebe um texto e deve devolver a assinatura do texto
    lista_sentencas = separa_sentencas(texto)
    
    lista_frases = [] 
    for sentenca in lista_sentencas:
        lista_frases += separa_frases(sentenca)

    lista_palavras = []
    for frase in lista_frases:
            lista_palavras += separa_palavras(frase)

    tamMedio = soma_qtd_char(lista_palavras)/len(lista_palavras)  # Tamanho médio de palavra
    typeToken = n_palavras_diferentes(lista_palavras)/len(lista_palavras)  # Relação Type-Token
    razaoHapaxL = n_palavras_unicas(lista_palavras)/len(lista_palavras)  # Razão Hapax Legomana
    tamMedioSen = tam_medio_sent(lista_sentencas)  # Tamanho médio de sentença
    complexSen = len(lista_frases)/len(lista_sentencas)  # Complexidade de sentença
    tamMedioFrase = soma_qtd_char(lista_frases)/len(lista_frases)  # Tamanho médio de frase

    return [tamMedio, typeToken, razaoHapaxL, tamMedioSen, complexSen, tamMedioFrase]


def avalia_textos(textos, ass_cp):
    # Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.

    lista_probabilidade = []
    for texto in textos:
        lista_probabilidade.append(compara_assinatura(calcula_assinatura(texto), ass_cp))

    min = lista_probabilidade[0]
    indexInf = 0
    i = 0
    while i < len(lista_probabilidade):
        if lista_probabilidade[i] < min:
            min = lista_probabilidade[i]
            indexInf = i
        i += 1
    return(indexInf+1)

def main():
    avalia_textos(le_textos(),le_assinatura())

if __name__ == "__main__":
    main()