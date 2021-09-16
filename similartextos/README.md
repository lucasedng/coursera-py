Atividade final proposta em [Introdução à Ciência da Computação com Python Parte 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos)
## Introdução

Manuel Estandarte é monitor na disciplina _Introdução à Produção Textual I_ na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

## Detecção de autoria

Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

## Traços linguísticos

Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

-   Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    
-   Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    
-   Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    
-   Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    
-   Complexidade de sentença: Média simples do número de frases por sentença.
    
-   Tamanho médio de frase: Média simples do número de caracteres por frase.
    

## Funcionamento do programa

A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

-   Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    
-   Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale $\frac{4}{5} = 0.8$
    
-   Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale $\frac{3}{5} = 0.6$
    
-   Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra **não** devem ser contabilizados como parte da sentença).
    
-   Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    
-   Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra **não** devem ser contabilizados como parte da frase).
    

Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, $a$ e $b$, é dado pela fórmula:

$S_{ab} = \frac{\sum_{i=1}^6 || f_{i,a} - f_{i,b} ||}{6}$

Onde:

-   $S_{ab}$ é o grau de similaridade entre os textos  $a$ e $b$ ;
    
-   $f_{i,a}$ é o valor de cada traço linguístico $i$ no texto $a$; e
    
-   $f_{i,b}$​ é o valor de cada traço linguístico $i$ no texto $b$.
    

No nosso caso, o texto $b$ não é conhecido, mas temos a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, sabemos o valor de $f_{i,b}$ que é dado como valor de entrada do programa.

Caso você não esteja acostumado com a notação matemática, podemos destrinchar essa fórmula da seguinte maneira:

Para cada traço linguístico $i$ (tamanho médio da palavra, relação type-token etc.) se quer a diferença entre o valor obtido em cada texto dado ($a$) e o valor típico do texto de uma pessoa infectada ($b$): $f_{i, a} - f_{i, b}$

Dessa diferença se toma o módulo ( $|| \ldots ||$), lembre-se da função _abs_ do python.

Somamos os resultados dos $6$ traços linguísticos ($\sum_{i=1}^6$)

E por final dividimos por 6 $( \frac{x}{6})$

Perceba que quanto mais similares $a$ e $b$ forem, menor $S_{ab}$ será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

## Exemplo de Assinatura

Um passo importante para seu programa é calcular a assinatura dos textos corretamente. Para testar se sua função **calcula_assinatura()** está correta, deixamos aqui um exemplo de execução:

>texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

>calcula_assinatura(texto)

>[4.507142857142857, 0.6928571428571428, 0.55, 70.81818181818181, 1.8181818181818181, 38.5]
