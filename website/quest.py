
import pandas as pd
import numpy as np
import regex as re
import json

quests ='''Q001	Até que série seu pai, ou o homem responsável por você, estudou?
	
		
Q002	Até que série sua mãe, ou a mulher responsável por você, estudou?
	
	
	
	
	
	
Q003	A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você. (Se ele não estiver trabalhando, escolha uma ocupação pensando no último trabalho dele).
	
	
		
Q004	A partir da apresentação de algumas ocupações divididas em grupos ordenados, indique o grupo que contempla a ocupação mais próxima da ocupação da sua mãe ou da mulher responsável por você. (Se ela não estiver trabalhando, escolha uma ocupação pensando no último trabalho dela).
	
	
	
	
	
Q005	Incluindo você, quantas pessoas moram atualmente em sua residência?
	
	
	
	
	

	
	
Q006	Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)
	
	
	

	
	
	
	
Q007	Em sua residência trabalha empregado(a) doméstico(a)?
	
	
	
Q008	Na sua residência tem banheiro?
	
	
	
	
Q009	Na sua residência tem quartos para dormir?
	
	
	
	
Q010	Na sua residência tem carro?
	
	
	
	
Q011	Na sua residência tem motocicleta?
	
	
	
	
Q012	Na sua residência tem geladeira?
	
	
	
	
Q013	Na sua residência tem freezer (independente ou segunda porta da geladeira)?
	
	
	
	
Q014	Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)
	
	
	
	
Q015	Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?
	
	
	
	
Q016	Na sua residência tem forno micro-ondas?
	
	
	
	
Q017	Na sua residência tem máquina de lavar louça?
	
	
	
	
Q018	Na sua residência tem aspirador de pó?
	
Q019	Na sua residência tem televisão em cores?
	
	
	
	
Q020	Na sua residência tem aparelho de DVD?
	
Q021	Na sua residência tem TV por assinatura?
	
Q022	Na sua residência tem telefone celular?
	
	
	
	
Q023	Na sua residência tem telefone fixo?
	
Q024	Na sua residência tem computador?
	
	
	
	
Q025	Na sua residência tem acesso à Internet? '''



quests = re.split("\t+|\n+",quests)

i = 0
while i < len(quests):
    if quests[i] == '':
        quests.remove(quests[i])
    else:
        i = i+1


i = 0

dictQuest = {}




answers = '''A	Nunca estudou.
B	Não completou a 4ª série/5º ano do Ensino Fundamental.
C	Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
D	Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
E	Completou o Ensino Médio, mas não completou a Faculdade.
F	Completou a Faculdade, mas não completou a Pós-graduação.
G	Completou a Pós-graduação.
H	Não sei.
A	Nunca estudou.
B	Não completou a 4ª série/5º ano do Ensino Fundamental.
C	Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.
D	Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.
E	Completou o Ensino Médio, mas não completou a Faculdade.
F	Completou a Faculdade, mas não completou a Pós-graduação.
G	Completou a Pós-graduação.
H	Não sei.
A	Grupo 1: Lavrador, agricultor sem empregados, bóia fria, criador de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultor, pescador, lenhador, seringueiro, extrativista.
B	Grupo 2: Diarista, empregado doméstico, cuidador de idosos, babá, cozinheiro (em casas particulares), motorista particular, jardineiro, faxineiro de empresas e prédios, vigilante, porteiro, carteiro, office-boy, vendedor, caixa, atendente de loja, auxiliar administrativo, recepcionista, servente de pedreiro, repositor de mercadoria.
C	Grupo 3: Padeiro, cozinheiro industrial ou em restaurantes, sapateiro, costureiro, joalheiro, torneiro mecânico, operador de máquinas, soldador, operário de fábrica, trabalhador da mineração, pedreiro, pintor, eletricista, encanador, motorista, caminhoneiro, taxista.
D	Grupo 4: Professor (de ensino fundamental ou médio, idioma, música, artes etc.), técnico (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretor de imóveis, supervisor, gerente, mestre de obras, pastor, microempresário (proprietário de empresa com menos de 10 empregados), pequeno comerciante, pequeno proprietário de terras, trabalhador autônomo ou por conta própria.
E	Grupo 5: Médico, engenheiro, dentista, psicólogo, economista, advogado, juiz, promotor, defensor, delegado, tenente, capitão, coronel, professor universitário, diretor em empresas públicas ou privadas, político, proprietário de empresas com mais de 10 empregados.
F	Não sei.
A	Grupo 1: Lavradora, agricultora sem empregados, bóia fria, criadora de animais (gado, porcos, galinhas, ovelhas, cavalos etc.), apicultora, pescadora, lenhadora, seringueira, extrativista.
B	Grupo 2: Diarista, empregada doméstica, cuidadora de idosos, babá, cozinheira (em casas particulares), motorista particular, jardineira, faxineira de empresas e prédios, vigilante, porteira, carteira, office-boy, vendedora, caixa, atendente de loja, auxiliar administrativa, recepcionista, servente de pedreiro, repositora de mercadoria.
C	Grupo 3: Padeira, cozinheira industrial ou em restaurantes, sapateira, costureira, joalheira, torneira mecânica, operadora de máquinas, soldadora, operária de fábrica, trabalhadora da mineração, pedreira, pintora, eletricista, encanadora, motorista, caminhoneira, taxista.
D	Grupo 4: Professora (de ensino fundamental ou médio, idioma, música, artes etc.), técnica (de enfermagem, contabilidade, eletrônica etc.), policial, militar de baixa patente (soldado, cabo, sargento), corretora de imóveis, supervisora, gerente, mestre de obras, pastora, microempresária (proprietária de empresa com menos de 10 empregados), pequena comerciante, pequena proprietária de terras, trabalhadora autônoma ou por conta própria.
E	Grupo 5: Médica, engenheira, dentista, psicóloga, economista, advogada, juíza, promotora, defensora, delegada, tenente, capitã, coronel, professora universitária, diretora em empresas públicas ou privadas, política, proprietária de empresas com mais de 10 empregados.
F	Não sei.
1	1, pois moro sozinho(a).
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
11	11
12	12
13	13
14	14
15	15
16	16
17	17
18	18
19	19
20	20
A	Nenhuma renda.
B	Até R$ 998,00.
C	De R$ 998,01 até R$ 1.497,00.
D	De R$ 1.497,01 até R$ 1.996,00.
E	De R$ 1.996,01 até R$ 2.495,00.
F	De R$ 2.495,01 até R$ 2.994,00.
G	De R$ 2.994,01 até R$ 3.992,00.
H	De R$ 3.992,01 até R$ 4.990,00.
I	De R$ 4.990,01 até R$ 5.988,00.
J	De R$ 5.988,01 até R$ 6.986,00.
K	De R$ 6.986,01 até R$ 7.984,00.
L	De R$ 7.984,01 até R$ 8.982,00.
M	De R$ 8.982,01 até R$ 9.980,00.
N	De R$ 9.980,01 até R$ 11.976,00.
O	De R$ 11.976,01 até R$ 14.970,00.
P	De R$ 14.970,01 até R$ 19.960,00.
Q	Mais de R$ 19.960,00.
A	Não.
B	Sim, um ou dois dias por semana.
C	Sim, três ou quatro dias por semana.
D	Sim, pelo menos cinco dias por semana.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim.
A	Não.
B	Sim, uma.
C	Sim, duas.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim.
A	Não.
B	Sim.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim.
A	Não.
B	Sim, um.
C	Sim, dois.
D	Sim, três.
E	Sim, quatro ou mais.
A	Não.
B	Sim.'''

answers = re.split("\t+|\n+",answers)



print()

answers2 = []
a = [[answers[1],0]]
dictionary = {}

df = pd.read_html("https://www.ibge.gov.br/explica/codigos-dos-municipios.php")

df = df[0]

df['Códigos'] = df['Códigos'].map(lambda x: x[0:2])

df = df.values.tolist()


dictionary['Qual é o seu estado de residencia?'] = df

array1_100 = np.arange(10,100,1).tolist()

while i < len(array1_100):
    array1_100[i] = [array1_100[i],array1_100[i]]
    i += 1

dictionary["Qual é a sua idade?"] = array1_100

dictionary["Ano em que você conclusão o Ensino Médio?"] = [["Não conclui antes do ENEM 2019",0],
        [2018,1],
        [2017,2],
        [2018,3],
        [2017,4],
        [2016,5],
        [2015,6],
    	[2014,7],
        [2013,8],
	    [2012,9],
	    [2011,10],
	    [2010,11],
	    [2009,12],
	    [2008,13],
	    [2007,14],
	    ["Antes de 2007",15]]

dictionary["Tipo de Sexo?"] = [["Masculino", 0], ["Feminino", 1]]

dictionary["É treneiro?"] = [["Sim", 1], ["Não",0]]

dictionary["Lingua Estrangeira?"] = [["Inglês", 0],["Espanhol", 1]]

k = 1
i = 2
j=1
while i < len(answers):
    if answers[i-1] == 'A' or answers[i-1] == '1':
        j += 1
        n = 0
        while n < len(a):
            a[n][1] = a[n][1]/(k)
            n = n+1
        a[k-1][1] = 1
        k = 0
        answers2.append(a)
        a = []
    if i%2 == 1:
        if answers[i] != "Não sei.":
            a.append([answers[i],k])
            k += 1
    i += 1

answers2.append(a)

j = 0
i = 0

while i < len(quests):
    if i%2==1:
        dictionary[quests[i]] = answers2[j]
        j+=1
    i += 1

json_object = json.dumps(dictionary,indent=4)
  
# Writing to sample.json
with open("public/quests.json", "w",encoding="utf-8") as outfile:
    outfile.write(json_object)
