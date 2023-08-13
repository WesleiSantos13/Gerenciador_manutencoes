# Autor: Weslei Silva Santos
# Componente Curricular: EXA854 MI - Algoritmos 
# Concluido em: 03/06/2021
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import os
from time import sleep
from datetime import date, timedelta
from collections import defaultdict


# Função para salvar o último valor do código da manutenção
def escrever_codigo_manutencao(codigo_da_manutencao):
    with open('Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Código da manutenção.txt', 'w') as arquivo9:
        arquivo9.write(f'{codigo_da_manutencao}')
        


# Função para salvar o último valor do código do cliente
def escrever_codigo_cliente(codigo_do_cliente):
    with open('Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Código do cliente.txt', 'w') as arquivo8:
        arquivo8.write(f'{codigo_do_cliente}')




# Função para ler o último valor do código da manutenção e do cliente
def ler_codigo_atual(nome_do_arquivo):
    with open(nome_do_arquivo, 'r') as arquivo9:
        # Transformando o arquivo em lista
        arquivo_lista0 = arquivo9.readlines()
        # Se o arquivo conter o código ele será carregado para o programa
        if not arquivo_lista0 == []:
            codigo_da_operacao = int(arquivo_lista0[0])
            
        # Se o arquivo estiver vazio o código do cliente será 1
        if arquivo_lista0 == []:
            codigo_da_operacao = 1
        return codigo_da_operacao

        
                 



# Função para ler os arquivos de manutenção e cliente 
def ler_arquivos(nome_do_arquivo):
    # Copiando os dados do arquivo para uma lista
    with open(nome_do_arquivo, 'r') as arquivo2:
      arquivo_lista = []
      for linha in arquivo2:
        # Retirando o \n
        linha_mod = linha.rstrip() 
        arquivo_lista.append(linha_mod)
   
    # Se a lista estiver vazia, O dicionário que irá armazenar os dados ficará vazio
    if arquivo_lista == []:
        dic = {}
        # Retornado o dicionário em uma tupla
        return dic

    # Se a lista conter informações, o programa irá ler a lista e passar as informações para o dicionário.
    if not arquivo_lista == []:
        dic = {}
        lista_de_codigos = []
        lista_de_informacoes = []
        for cont in range(0, len(arquivo_lista)):
            if cont % 2 == 0:
                # Adicionando os códigos do arquivo na lista de códigos
                lista_de_codigos.append(arquivo_lista[cont])
            else:
                # Adicionando as informações do arquivo na lista de informações
                lista_de_informacoes.append(arquivo_lista[cont])
                      
        for cont in range(0, len(lista_de_codigos)):
            # Adicionando os códigos como chave e as informações como valor 
            dic[int(lista_de_codigos[cont])] = lista_de_informacoes[cont]

        # Retornado o dicionário
        return dic


# Função para ler os códigos de clientes ou manutenções que o usuário deseja excluir, editar, listar ou realizar
def fazer_operacoes():
  edicao = ' '
  while type(edicao) != int:
    try:
      edicao = int(input('Código: '))
    except ValueError:
        print('Digite um número inteiro!')
  return edicao 

# Função para escrever as manutenções realizadas no arquivo
def escrever_manutencoes_realizadas(manutencoes_realizadas):
     with open('Arquivos/Pasta de leitura e armazenamento de dados/Manutenções/Manutenções realizadas.txt', 'w') as arquivo2:
      for elemento in manutencoes_realizadas:  
        arquivo2.write(f'{elemento}\n')
        arquivo2.write(f'{manutencoes_realizadas[elemento]}\n')
      

# Função para apagar as informações dos dicionários, que contém o código com os dados da manutenção separados    
def apagar_informaões(edicao, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente):
    data = codigos_datas.pop(edicao)
    custo = codigos_custos.pop(edicao)
    peça = codigos_peca.pop(edicao)
    prazo = codigos_prazo.pop(edicao)
    cliente = codigos_cliente.pop(edicao)
    # Retornado informações apagadas em uma tupla
    return (data, custo, peça, prazo, cliente)


# Função para adicionar o código junto aos dados da manutenção em dicionários(SEPARADAMENTE)
def dados_da_manutencao_separados(manutencao, codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente):
    # Dicionário contendo os códigos da manutenção com as datas de agendamento 
    codigos_datas[codigo_mutavel]   = manutencao['Data agendada'] 
    # Dicionário contendo os códigos da manutenção com os custos  
    codigos_custos[codigo_mutavel]  = manutencao['Custo da manutenção']
    # Dicionário contendo os códigos da manutenção com o nome da peça
    codigos_peca[codigo_mutavel] = manutencao['Nome da peça'] 
    # Dicionário contendo os códigos da manutenção com os prazos de validade  
    codigos_prazo[codigo_mutavel]   = manutencao['Prazo de validade'] 
    # Dicionário contendo os códigos da manutenção com os códigos dos clientes
    codigos_cliente[codigo_mutavel] = manutencao['Cliente'] 


# Função para escrever os dicionários com os dados da manutenção no arquivo
def escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente):
  with open('Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Códigos das manutenções com suas respectivas informações.txt', 'w') as arquivo5:
    for elemento in codigos_datas:  
        arquivo5.write(f'{elemento}\n')
        arquivo5.write(f'{codigos_datas[elemento]}\n')

    for elemento in codigos_custos:
        arquivo5.write(f'{elemento}\n')
        arquivo5.write(f'{codigos_custos[elemento]}\n')

    for elemento in codigos_peca:
        arquivo5.write(f'{elemento}\n')
        arquivo5.write(f'{codigos_peca[elemento]}\n')

    for elemento in codigos_prazo:
        arquivo5.write(f'{elemento}\n')
        arquivo5.write(f'{codigos_prazo[elemento]}\n')

    for elemento in codigos_cliente:
        arquivo5.write(f'{elemento}\n')
        arquivo5.write(f'{codigos_cliente[elemento]}\n')


# Função para mostrar o balanço do mês
def mostrar_balaco_do_mes(manutencoes_realizadas):    

    # Data para fazer o balanço 
    mes = input('Digite o mês que deseja fazer o balanço. Formato: 03   - ')
    ano = input('Digite o ano que deseja fazer o balanço. Formato: 2021 - ')
    data_balanco = f'{ano}/{mes}'
 
    rendimento_do_mes = 0
    lista_de_manutecoes_realizadas = []

    # Lista com as datas de realização da manutenção
    lista_com_datas = []

    # Lista com todas as manutenções do mês
    manutençoes_do_mes = []

    for chave, valor in manutencoes_realizadas.items():
        lista_de_manutecoes_realizadas.append(f'{chave}:{valor}')
    for elemento in lista_de_manutecoes_realizadas:
        # Encontrando a data das manuteções realizadas
        encontrar_ano_mes = elemento.split()
        encontrar_ano_mes = encontrar_ano_mes[2]
        encontrar_ano_mes = encontrar_ano_mes[1:8]
        # Adicionando as datas em uma lista
        lista_com_datas.append(encontrar_ano_mes)


    # A variável 'DATAS' irá colecionar as posicões dos elementos da 'lista_com_datas' numa lista, como valor no dicionário, junto com as datas como chave
    DATAS = defaultdict(list)
    # Enumerando os valores da lista
    for POSICAO, DATA in enumerate(lista_com_datas):
        # Encontrando as posições das datas e adicionando na coleção 
        DATAS[DATA].append(POSICAO)

    # OBS: A IDEIA PRINCIPAL DO MÉTODO 'defaultdict(list)' FOI TIRADO DO SITE ABAIXO:
    # https://pt.stackoverflow.com/questions/216413/identificar-elementos-repetidos-em-lista-com-python
    

    # Fazendo o balanço do mês se baseando no mês e ano dados  
    for elemento in DATAS[data_balanco]:
        manutencao_realizada = (lista_de_manutecoes_realizadas[elemento])
        # As manutenções da data dada são adicionadas em uma lista
        manutençoes_do_mes.append(manutencao_realizada)

    # Pegando os rendimentos de cada manutenção
    for elemento in manutençoes_do_mes:
        elemento = elemento.split()
        elemento= elemento[6] 
        custo_das_manutencoes = elemento[:len(elemento)-1]        
        rendimento_do_mes += float(custo_das_manutencoes)      

    # Escrevendo o balanço do mês no arquivo
    with open('Arquivos/Pasta direcionada ao usuário/Balanço do mês.txt', 'w') as arquivo7:
      arquivo7.write('         BALANÇO DO MÊS :\n')
      arquivo7.write('\n')
      arquivo7.write(f'MANUTENÇÕES REALIZADAS EM {data_balanco}:\n')
      arquivo7.write('\n')
      for elemento in manutençoes_do_mes:  
        arquivo7.write(f'{elemento}\n')
      arquivo7.write('\n')
      arquivo7.write(f'Rendimento do mês: {rendimento_do_mes} reais\n')
      os.system('cls')

      print(' ')
      print(f'Manutenções realizadas em {data_balanco}')
      print(' ')
      for elemento in manutençoes_do_mes:
          print(f'{elemento}')
      print(' ')
      print(f'Rendimento do mês: {rendimento_do_mes} Reais')


# Função para escrever manutenções no arquivo
def escrever_manutencoes_arquivo(manutencoes_agendadas):
  with open('Arquivos/Pasta de leitura e armazenamento de dados/Manutenções/Manutenções agendadas.txt', 'w') as arquivo2:
      for elemento in manutencoes_agendadas:  
        arquivo2.write(f'{elemento}\n')
        arquivo2.write(f'{manutencoes_agendadas[elemento]}\n')

  # Imprimindo manutenções ordenadas por data para o arquivo
  with open('Arquivos/Pasta direcionada ao usuário/Imprimir manutenções.txt', 'w') as arquivo2:
      arquivo2.write('         LISTA DE MANUTENÇÕES ORDENADAS POR DATA :\n')
      arquivo2.write('\n')
      lista_ordenada = []
      for chave, valor in manutencoes_agendadas.items():
          lista_ordenada.append(f'{valor} -Código da manutenção:{chave}')

      # Ordenação Insertion Sort
      tamanho = len(lista_ordenada)
      for i in range(1, tamanho):
        aux = lista_ordenada[i]
        j = i - 1
        while j >=0 and aux < lista_ordenada[j]:
           lista_ordenada[j+1] = lista_ordenada[j]
           j -= 1
        lista_ordenada[j+1] = aux  #  OBS: Esse método de ordenação foi tirado do slide do link abaixo:
                                   #  https://drive.google.com/file/d/1Hu6HUsfCNfRhaMRwm-Ysh_lw_B_1m22t/view
                                   #  Slide encontrado em: https://sites.google.com/view/ap1uefs20201/aulas
                                   #  Autora: Claudia Pinto Pereira
        
        
      for elemento in lista_ordenada:
        arquivo2.write(f'{elemento}\n')




# Função para passar os dados do cliente para o arquivo
def escrever_clientes_arquivo(clientes_registrados):
  with open('Arquivos/Pasta de leitura e armazenamento de dados/Clientes Cadastrados.txt', 'w') as arquivo:
      for elemento in clientes_registrados:  
        arquivo.write(f'{elemento}\n')
        arquivo.write(f'{clientes_registrados[elemento]}\n')

  # Arquivo para a visualização do usuário
  with open('Arquivos/Pasta direcionada ao usuário/Listagem de clientes.txt', 'w') as arquivo:
      arquivo.write('         LISTA DE CLIENTES :\n')
      arquivo.write('\n')
      for elemento in clientes_registrados:  
        arquivo.write(f'CÓDIGO:{elemento}|INFORMAÇÕES:{clientes_registrados[elemento]}\n')




# Função para registrar os dados da manutenção
def dados_manutencao():
  # Dicionário Temporário
  manutencao = {}

  # Registro da data
  manutencao['Data agendada'] = input('Digite a data que deseja realizar sua manutenção. Formato:(2021/05/11) ')

  # Registro do custo da manutenção 
  manutencao['Custo da manutenção'] = ' '
  while type(manutencao['Custo da manutenção'] ) != float:
      try:
        manutencao['Custo da manutenção'] = float(input('Custo da manutenção '))
      except ValueError:
        print('Digite um número inteiro ou decimal!')

  # Registro do nome da peça
  manutencao['Nome da peça'] = input('Nome da peça ')

  # Registro do prazo de validade da peça
  manutencao['Prazo de validade'] = ' '
  while type(manutencao['Prazo de validade']) != int:
      try:
        manutencao['Prazo de validade'] = int(input('Prazo de validade em meses. Formato: 3, 12 '))
      except ValueError:
        print('Digite um número inteiro!')

  # Registro do código do cliente
  manutencao['Cliente'] = ' '
  while type(manutencao['Cliente']) != int:
    try:
      manutencao['Cliente'] = int(input('Codigo do Cliente '))
    except ValueError:
        print('Digite um número inteiro!')        
  return manutencao





# Função para registrar os dados do cliente
def dados_cliente():
  # Dicionário Temporário
  cliente = {}
  cliente['Nome'] = input('Nome: ').upper()
  cliente['Endereço'] = input('Endereço: ').upper()
  cliente['Telefone'] = input('Telefone:')
  return cliente
 

# Função para mostrar a lista de clientes ordenada
def tabela_clientes(clientes_registrados):
  lista_ordenada = []

  print('                    LISTA DE CLIENTES EM ORDEM ALFABÉTICA:                            ')    
  for chave, valor in clientes_registrados.items():
   lista_ordenada.append(f'{valor} -Código do cliente:{chave}')

  # Ordenação Insertion Sort
  tamanho = len(lista_ordenada)
  for i in range(1, tamanho):
    aux = lista_ordenada[i]
    j = i - 1
    while j >=0 and aux < lista_ordenada[j]:
       lista_ordenada[j+1] = lista_ordenada[j]
       j -= 1
    lista_ordenada[j+1] = aux   #  OBS: Esse método de ordenação foi tirado do slide do link abaixo:
                                   #  https://drive.google.com/file/d/1Hu6HUsfCNfRhaMRwm-Ysh_lw_B_1m22t/view
                                   #  Slide encontrado em: https://sites.google.com/view/ap1uefs20201/aulas
                                   #  Autora: Claudia Pinto Pereira

  for elemento in lista_ordenada:
      print(elemento)

  


# Função para mostrar as manutenções agendadas
def mostrar_manutencoes_agendadas(manutencoes_agendadas):

    # Manutenções agendadas
    print('________________________________________________________________________________________')
    print('|CÓD |              INFORMAÇÕES DAS MANUTENÇÕES AGENDADAS                              |')    
    for chave, valor in manutencoes_agendadas.items():
        print(f'|{chave}|{valor}')



# Função para mostrar as manutenções realizadas
def mostrar_manutencoes_realizadas(manutencoes_realizadas):
    # Manutenções realizadas
    print('________________________________________________________________________________________')
    print('|CÓD |              INFORMAÇÕES DAS MANUTENÇÕES REALIZADAS                          |')    
    for chave, valor in manutencoes_realizadas.items():
        print(f'|{chave}|{valor}')    



# Função para chamar o menu de funções
def menu():
  print('--------------------------------------')
  print('     GERENCIADOR DE MANUTENÇÕES       ')
  print('--------------------------------------')
  print('|       O QUE DESEJA FAZER ?         |')
  print('|------------------------------------|')
  print('|(1) Registrar um novo cliente       |')
  print('|------------------------------------|')
  print('|(2) Editar dados do cliente         |')
  print('|------------------------------------|')
  print('|(3) Excluir um cliente              |')
  print('|------------------------------------|')
  print('|(4) Listar clientes                 |')
  print('|------------------------------------|')
  print('|(5) Registrar uma nova manutenção   |')
  print('|------------------------------------|')
  print('|(6) Editar dados da manutenção      |')
  print('|------------------------------------|')
  print('|(7) Excluir uma manutenção          |')
  print('|------------------------------------|')
  print('|(8) Realizar uma manutenção         |')
  print('|------------------------------------|')
  print('|(9) Listar manutenções              |')
  print('|------------------------------------|')
  print('|(10) Balanço do mês                 |')
  print('|------------------------------------|')    
  print('|(0) Sair                            |')
  print('--------------------------------------')
  verificador_resposta = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
  resposta = input('-')
  # Estratégia para evitar erros
  while resposta not in verificador_resposta:
     resposta = input('-')
  os.system('cls')
  return resposta
  



# Função para registrar um novo cliente
def novo_cliente(clientes_registrados, codigo_do_cliente): 
  cliente = dados_cliente()   
  # Registrando cliente no dicionário
  clientes_registrados[codigo_do_cliente] = cliente    
  # Escrevendo o dicionário de clientes no arquivo
  escrever_clientes_arquivo(clientes_registrados)
  print('Cliente registrado com sucesso')
  sleep(2)
  os.system('cls')




# Função para editar dados do cliente
def editar_cliente(clientes_registrados): 
  print('Insira o código do cliente que você deseja editar')
  edicao = fazer_operacoes()
  # Se o código digitado não existir, não haverá erro
  if clientes_registrados.get(edicao) == None:
    print('Código inexistente')
    sleep(2)

  # Se o código digitado existir, o dados antigos serão substituidos
  else:
    os.system('cls')
    print('Atualização do cadastro :')
    # Um novo registro é gerado
    cliente = dados_cliente()

    # Depois o registro é adicionado no dicionário
    clientes_registrados[edicao] = cliente
    print('Cliente atualizado com sucesso')

    # Escrevendo o dicionário de clientes no arquivo
    escrever_clientes_arquivo(clientes_registrados)
    sleep(2)
  os.system('cls')

 



# Função para excluir dados do cliente
def excluir_cliente(clientes_registrados):  
  print('Insira o código do cliente que você deseja excluir')   
  excluir = fazer_operacoes()

  # Criando um dicionário para verificar a viculação entre cliente e manutenção
  verificar_vinculacao = {}
  for chave, valor in codigos_cliente.items():
    verificar_vinculacao[valor] = chave


  # Se código não existir, não haverá erro
  if clientes_registrados.get(excluir) == None:
    print('Código inexistente')
    sleep(2)

  # Se código do cliente existir..
  else:
      # Se o código do cliente estiver no dicionário junto com as manutenções, não será possivel excluir o cliente   
      if excluir in verificar_vinculacao:
        print('Impossivel excluir este cliente, pois ele está vinculado a manutenções')
        sleep(2)
      # Se código do cliente existir e não estiver vinculado a manutenções, o cliente será excluído
      else:
        clientes_registrados.pop(excluir)
        print('Cliente excluido com sucesso')
        sleep(2)

      # Escrevendo o dicionário de clientes no arquivo
      escrever_clientes_arquivo(clientes_registrados)
      os.system('cls')







def listar_clientes(clientes_registrados):
    print('Digite:')
    print('(U) Para listar apenas um cliente') 
    print('(T) Para listar todos os clientes ')
    pergunta = input('- ').upper()
    while pergunta != 'U' and pergunta != 'T':
        pergunta = input('- ').upper()
    os.system('cls')

    # Mostrar todos os clientes
    if pergunta == 'T': 
      tabela_clientes(clientes_registrados)      

    # Mostrar apenas um cliente 
    elif pergunta == 'U': 
        print('Digite o código do cliente que deseja ver ')
        ver = fazer_operacoes()    
        exibir = clientes_registrados.get(ver)
        if exibir == None:
            print('Código inexistente')
            sleep(2)
            os.system('cls')
        else:
           print(f'{ver}:{exibir}')
  




# Função para registrar uma nova manutenção
def nova_manutencao(manutencoes_agendadas, codigo_da_manutencao):
  manutencao = dados_manutencao()

  # A variável 'codigo_mutavel' foi feito para adequar a modularização 'dados_da_manutencao_separados' para outros procedimentos
  codigo_mutavel = codigo_da_manutencao
  # Adicionando as informações da manutenção separadamente em dicionários
  dados_da_manutencao_separados(manutencao, codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)

  # Registrando manutenção no dicionário principal de manutenções
  manutencoes_agendadas[codigo_da_manutencao] = manutencao
  # Escrevendo as manutenções agendadas no arquivo
  escrever_manutencoes_arquivo(manutencoes_agendadas)
  # Escrevendo as informações da manutenção separadamente no arquivo
  escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
  print('Manutenção criada com sucesso')
  sleep(2)
  os.system('cls')




  

# Função para editar os dados da manutenção
def editar_manutencao(manutencoes_agendadas):
  print('Insira o código da manutenção que você deseja editar')
  edicao = fazer_operacoes()

  # Se código não existir, não haverá erro
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
    sleep(2)
    os.system('cls')
  # Se código da manutenção existir, os dados serão editados
  else:
    manutencao = dados_manutencao()

    # A variável 'codigo_mutavel' irá receber o codigo da manutenção que o usuário deseja editar
    codigo_mutavel = edicao
    # Adicionando as informações da manutenção separadamente em dicionários
    dados_da_manutencao_separados(manutencao, codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    # Registrando manutenção no dicionário principal de manutenções
    manutencoes_agendadas[edicao] = manutencao

    # Escrevendo as manutenções agendadas no arquivo
    escrever_manutencoes_arquivo(manutencoes_agendadas)
    # Escrevendo as informações da manutenção separadamente no arquivo
    escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    print('Manutenção editada com sucesso')
    sleep(2)
    os.system('cls')    





# Função para excluir manutenção
def excluir_manutencao(manutencoes_agendadas): 
  print('Insira o código da manutenção que você deseja excluir')   
  edicao = fazer_operacoes()

  # Se código não existir, não haverá erro
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
    sleep(2)
    os.system('cls')
  else:
    # A variável 'codigo_mutavel' irá receber o codigo da manutenção que o usuário deseja excluir
    codigo_mutavel = edicao
    # Apagando as informações da manutenção que estão contidos nos dicionários de informações
    deletar = apagar_informaões(codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    # Apagando manutenção do dicionário principal de manutenções
    manutencoes_agendadas.pop(edicao)

    # Escrevendo as manutenções agendadas no arquivo
    escrever_manutencoes_arquivo(manutencoes_agendadas)
    # Escrevendo as informações da manutenção separadamente no arquivo
    escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    print('Manutenção excluida com sucesso')
    sleep(2)
    os.system('cls')






# Função para realizar uma nova manutenção
def realizar_manutencao(manutencoes_agendadas, manutencoes_realizadas, codigo_da_manutencao):
  print('Insira o código da manutenção que você deseja realizar')   
  edicao = fazer_operacoes()

  # Se código não existir, não haverá erro
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
    sleep(2)
    os.system('cls')

  else:
    # Apagando os dados da manutenção do dicionário de informações e salvando os dados apagados
    tupla_informacoes = apagar_informaões(edicao, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    data = tupla_informacoes[0] # Essa informação da data não será usada
    custo = tupla_informacoes[1]
    peça = tupla_informacoes[2]
    prazo = tupla_informacoes [3]
    cliente = tupla_informacoes[4]

    # Copiando a manutenção agendada para o dicionário de manutenções realizadas
    manutencoes_realizadas[edicao] = manutencoes_agendadas[edicao]
    # Removendo a manutenção do dicionário de manutenções agendadas
    manutencoes_agendadas.pop(edicao)

    # Escrevendo as manutenções realizadas no arquivo
    escrever_manutencoes_realizadas(manutencoes_realizadas)
    # Escrevendo as manutenções agendadas no arquivo
    escrever_manutencoes_arquivo(manutencoes_agendadas)
    # Escrevendo as informações da manutenção separadamente no arquivo
    escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
    print('Manutenção realizada com sucesso')
    sleep(2)
    os.system('cls')


    # Agendamento
    pergunta = input('Deseja marcar uma nova manutenção (s) ou (n) ?').upper()
    while pergunta != 'S' and pergunta != 'N':
        pergunta = input('Deseja marcar uma nova manutenção (s) ou (n) ?').upper()

    # Se o usuário quiser agendar a próxima manutenção da peça irá perguntar a forma de agendamento
    if pergunta == 'S':

      # O usuário poderá escolher se quer agendar manualmente ou automaticamente
      pergunta2 = input('Deseja marcar automaticamente ou manualmente? (a) ou (m) ?').upper()
      while pergunta2 != 'A' and pergunta2 != 'M':
          pergunta2 = input('Deseja marcar automaticamente ou manualmente? (a) ou (m) ?').upper()    

    # Agendamento manual
      if pergunta2 == 'M':
        manutencao = {}
        # Registro de uma nova manutenção
        manutencao['Data agendada'] = input('Digite a data que deseja realizar sua manutenção - Formato:(2021/05/11) ')
        
        manutencao['Custo da manutenção'] = ' '
        while type(manutencao['Custo da manutenção'] ) != float:
            try:
                manutencao['Custo da manutenção'] = float(input('Custo da manutenção '))
            except ValueError:
                print('Digite um número inteiro ou decimal!')

        manutencao['Nome da peça'] = input('Nome da peça ')

        manutencao['Prazo de validade'] = ' '
        while type(manutencao['Prazo de validade']) != int:
            try:
                manutencao['Prazo de validade'] = int(input('Prazo de validade '))
            except ValueError:
                print('Digite um número inteiro!')

        # O usuário não poderá digitar o código do cliente, pois o código do cliente será o mesmo da manutenção realizada
        manutencao['Cliente'] = cliente
        # Registrando manutenção no dicionário principal de manutenções
        manutencoes_agendadas[codigo_da_manutencao] = manutencao
        # A variável 'codigo_mutavel' irá receber o codigo da manutenção atual
        codigo_mutavel = codigo_da_manutencao
        # Adicionando as informações da manutenção separadamente em dicionários
        dados_da_manutencao_separados(manutencao, codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)

    # Agendamento automático
      elif pergunta2 == 'A':
        # Trasformando o prazo de validade de meses para dias
        dias = prazo*30
        # Pegando a data de realização da manutenção
        hoje = date.today()
        # Somando a data de realização com o prazo de validade
        data_agendada = hoje + timedelta(days=dias)
        
        manutencao = {}
        # A data somada será adicionada no dicionário e as informações deletadas anteriormente dos dicionários de dados serão usadas em uma nova manutenção agendada
        manutencao['Data agendada'] = data_agendada.strftime('%Y/%m/%d')
        manutencao['Custo da manutenção'] = custo
        manutencao['Nome da peça'] = peça
        manutencao['Prazo de validade'] = prazo
        manutencao['Cliente'] = cliente
        # Registrando manutenção no dicionário principal de manutenções
        manutencoes_agendadas[codigo_da_manutencao] = manutencao

        # A variável 'codigo_mutavel' irá receber o codigo da manutenção atual
        codigo_mutavel = codigo_da_manutencao
        # Adicionando as informações da manutenção separadamente em dicionários
        dados_da_manutencao_separados(manutencao, codigo_mutavel, codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
      # Escrevendo as manutenções agendadas no arquivo
      escrever_manutencoes_arquivo(manutencoes_agendadas)
      # Escrevendo as informações da manutenção separadamente no arquivo
      escrever_codigos_de_manutencoes_e_informações(codigos_datas, codigos_custos, codigos_peca, codigos_prazo, codigos_cliente)
      print('Manutenção criada com sucesso')
      sleep(2)
      os.system('cls')      

      return pergunta










# Programa pricipal    

# Lendo o arquivo contendo os dados da manutenção, junto com os códigos das manutenções 
with open('Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Códigos das manutenções com suas respectivas informações.txt', 'r') as arquivo5:
    # Tranformando o arquivo em lista
    arquivo_lista5 = []
    for linha in arquivo5:
        # Retirando o \n
        linha_mod = linha.rstrip() 
        arquivo_lista5.append(linha_mod)

# Criando dicionários
codigos_datas = {}
codigos_custos = {}
codigos_peca = {}
codigos_prazo = {}
codigos_cliente = {}


if not arquivo_lista5 == []:       
    lista_de_datas = []
    lista_de_custos = []
    lista_de_pecas = []
    lista_de_prazos = []
    lista_de_cod_clientes = []
    tamanho = int(len(arquivo_lista5)/5)

    # Pegando os códigos e datas da manutenção e adicionando em 'lista_de_datas'
    for cont in range(0, tamanho):
        lista_de_datas.append(arquivo_lista5[cont])
    # Pegando os códigos e custos das manutenções e adicionando em 'lista_de_custos'
    for cont in range(tamanho, tamanho*2):
        lista_de_custos.append(arquivo_lista5[cont])
    # Pegando os códigos e o nome das peças da manutenção e adicionando em 'lista_de_pecas'
    for cont in range(tamanho*2, tamanho*3):
        lista_de_pecas.append(arquivo_lista5[cont])
    # Pegando os códigos e os prazos de validade da manutenção e adicionando em 'lista_de_prazos'
    for cont in range(tamanho*3, tamanho*4):
        lista_de_prazos.append(arquivo_lista5[cont])
    # Pegando os códigos da manutenção e do cliente e adicionando em 'lista_de_cod_clientes '
    for cont in range(tamanho*4, tamanho*5):
        lista_de_cod_clientes.append(arquivo_lista5[cont])
          

    # Passando os dados para dicionários
    # Pegando os códigos presentes na lista e transformando em chave e as informações da manutenção em valor
    for cont in range(0, len(lista_de_datas)):
        if cont % 2 == 0:
            codigos_datas[int(lista_de_datas[cont])] = lista_de_datas[cont+1]


    for cont in range(0, len(lista_de_custos)):
        if cont % 2 == 0:
            codigos_custos[int(lista_de_custos[cont])] = lista_de_custos[cont+1]


    for cont in range(0, len(lista_de_pecas)):
        if cont % 2 == 0:
            codigos_peca[int(lista_de_pecas[cont])] = lista_de_pecas[cont+1]

    for cont in range(0, len(lista_de_prazos)):
        if cont % 2 == 0:
            codigos_prazo[int(lista_de_prazos[cont])] = int(lista_de_prazos[cont+1])

    for cont in range(0, len(lista_de_cod_clientes)):
        if cont % 2 == 0:
            codigos_cliente[int(lista_de_cod_clientes[cont])] = int(lista_de_cod_clientes[cont+1])
     
       





# Chamando a função para ler o arquivo com os clientes registrados
nome_do_arquivo = 'Arquivos/Pasta de leitura e armazenamento de dados/Clientes Cadastrados.txt'
dicionario = ler_arquivos(nome_do_arquivo)
# Extraindo informações para o dicionário de clientes registrados
clientes_registrados = dicionario

# Chamando a função para ler o arquivo com o código do cliente
nome_do_arquivo =  'Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Código do cliente.txt'
# Extraindo informações para a variável 'codigo_do_cliente'
codigo_do_cliente  = ler_codigo_atual(nome_do_arquivo)




# Chamando a função para ler o arquivo com as manutenções agendadas
nome_do_arquivo = 'Arquivos/Pasta de leitura e armazenamento de dados/Manutenções/Manutenções agendadas.txt'
dicionario = ler_arquivos(nome_do_arquivo)
# Extraindo informações para o dicionário de manutenções agendadas
manutencoes_agendadas = dicionario

nome_do_arquivo = 'Arquivos/Pasta de leitura e armazenamento de dados/Estratégia para o funcionamento do programa/Código da manutenção.txt'
# Extraindo informações para a variável 'codigo_da_manutencao'
codigo_da_manutencao = ler_codigo_atual(nome_do_arquivo)



# Chamando a função para ler o arquivo com as manutenções realizadas
nome_do_arquivo = 'Arquivos/Pasta de leitura e armazenamento de dados/Manutenções/Manutenções realizadas.txt'
dicionario = ler_arquivos(nome_do_arquivo)
# Extraindo informações para o dicionário de manutenções realizadas
manutencoes_realizadas = dicionario





resposta = menu()
# Menu principal
while resposta != '0':
  
  # Novo cliente
  if resposta == '1':
   novo_cliente(clientes_registrados, codigo_do_cliente)
   codigo_do_cliente += 1
   escrever_codigo_cliente(codigo_do_cliente)
   resposta = menu()
  
  # Editar cliente 
  elif resposta == '2':  
    tabela_clientes(clientes_registrados)
    edicao = editar_cliente(clientes_registrados)
    resposta = menu()
   
  # Excluir cliente
  elif resposta == '3':
    tabela_clientes(clientes_registrados)
    excluir_cliente(clientes_registrados)
    resposta = menu()

  # Listar clientes
  elif resposta == '4':
    listar_clientes(clientes_registrados)
    resposta = menu()
  
  # Nova manutenção
  elif resposta == '5':
    nova_manutencao(manutencoes_agendadas, codigo_da_manutencao)
    codigo_da_manutencao += 1    
    escrever_codigo_manutencao(codigo_da_manutencao)
    resposta = menu()
  
  # Editar manutenção
  elif resposta == '6':
    mostrar_manutencoes_agendadas(manutencoes_agendadas)
    editar_manutencao(manutencoes_agendadas)
    resposta = menu()
    
  # Excluir manutenção
  elif resposta == '7':
    mostrar_manutencoes_agendadas(manutencoes_agendadas)
    excluir_manutencao(manutencoes_agendadas)
    resposta = menu()
  
  # Realizar manutenção
  elif resposta == '8':
    mostrar_manutencoes_agendadas(manutencoes_agendadas)
    pergunta = realizar_manutencao(manutencoes_agendadas, manutencoes_realizadas, codigo_da_manutencao)
    # Se a manutenção foi realizada e marcada novamente, o código da manutenção será incrementado 
    if pergunta == 'S':
       codigo_da_manutencao += 1 
       escrever_codigo_manutencao(codigo_da_manutencao)
    resposta = menu()

  # Listar manutenções
  elif resposta == '9':
    mostrar = input('Que tipo de manutenção deseja ver? Realizadas(R) ou Agendadas(A)? -').upper()

    while mostrar != 'R' and mostrar != 'A':
        mostrar = input('Que tipo de manutenção deseja ver? Realizadas(R) ou Agendadas(A)? -').upper()
    if mostrar == 'A':
        mostrar_manutencoes_agendadas(manutencoes_agendadas)
    else:
        mostrar_manutencoes_realizadas(manutencoes_realizadas)
    resposta = menu()

  # Balanço do mês 
  elif resposta == '10':
    mostrar_balaco_do_mes(manutencoes_realizadas)
    resposta = menu()
    

if resposta == '0':
  print('Fim do Registro')
  sleep(3)
