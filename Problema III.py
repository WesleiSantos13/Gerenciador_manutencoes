import os
from time import sleep

# COPIANDO OS DADOS DO ARQUIVO PARA UMA LISTA
with open('Arquivos/clientes.txt', 'r') as arquivo:
  arquivo_lista = []
  for linha in arquivo:
    linha_mod = linha.rstrip() 
    arquivo_lista.append(linha_mod)


with open('Arquivos/clientes.txt', 'r') as arquivo:   
  # SE O ARQUIVO ESTIVER VAZIO O CÓDIGO SERÁ 1.
  if arquivo_lista == []:
    clientes_registrados = {}
    codigo_do_cliente = 1

  # SE O ARQUIVO CONTER INFORMAÇÕES, O PROGRAMA IRA LER O ARQUIVO E PASSAR AS INFORMAÇÕES PARA O DICIONÁRIO.
  if not arquivo_lista == []:
    clientes_registrados = {}
    print('------------ARQUIVO LIDO--------------')
    dados_arquivo = []
    for linha in arquivo:
      dados_arquivo.append(linha.rstrip())

    lista_de_codigos = []
    lista_de_informacoes = []
    for cont in range(0, len(dados_arquivo)):
      if cont % 2 == 0:
          lista_de_codigos.append(dados_arquivo[cont])
      else:
          lista_de_informacoes.append(dados_arquivo[cont])
    
    for cont in range(0, len(lista_de_codigos)):
        clientes_registrados[int(lista_de_codigos[cont])] = lista_de_informacoes[cont]
    # GERANDO O PROXIMO CÓDIGO
    codigo_do_cliente = int(lista_de_codigos[len(lista_de_codigos)-1])
    codigo_do_cliente +=1

listagem_clientes = {}
manutencoes_realizadas = {}
manutencoes_agendadas = {}


codigo_da_manutencao = 1
# Função para passar os dados do cliente para o arquivo
def escrever_clientes_arquivo(clientes_registrados):
  with open('Arquivos/clientes.txt', 'w') as arquivo:
      for elemento in clientes_registrados:  
        arquivo.write(f'{elemento}\n')
        arquivo.write(f'{clientes_registrados[elemento]}\n')

  with open('Arquivos/Pasta direcionada ao usuário/Listagem de clientes.txt', 'w') as arquivo:
      arquivo.write('         LISTA DE CLIENTES :\n')
      arquivo.write('\n')
      for elemento in clientes_registrados:  
        arquivo.write(f'CÓDIGO:{elemento}|INFORMAÇÕES:{clientes_registrados[elemento]}\n')

def dados_manutencao():
  manutencao = {}
  manutencao['Custo da peça'] = input('Custo da peça ')
  manutencao['Nome da peça'] = input('Nome da peça ')
  manutencao['Prazo de validade'] = input('Prazo de validade ')
  manutencao['Cliente'] = int(input('Codigo do Cliente '))
  return manutencao

def dados_cliente():
  cliente = {}
  cliente['Nome'] = input('Nome: ').upper()
  cliente['Endereço'] = input('Endereço: ').upper()
  cliente['Telefone'] = input('Telefone:')
  return cliente
 

def tabela(clientes_registrados):
  print('________________________________________________________________________________________')
  print('|CÓDIGO |                    INFORMAÇÕES DO CLIENTE                                     |')    
  for chave, valor in clientes_registrados.items():
    print(f'|{chave}|{valor}')

# Função para chamar o menu
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
  print('|(0) Sair                            |')
  print('--------------------------------------')
  resposta = input('-')
  while resposta not in '123456789010' or resposta == '':
     resposta = input('-')
  os.system('cls')
  return resposta
  
# Função para registrar um novo cliente
def novo_cliente(listagem_clientes, clientes_registrados, codigo_do_cliente): 
  cliente = dados_cliente()   
  clientes_registrados[codigo_do_cliente] = cliente    
  listagem_clientes[cliente['Nome']] = {'Endereço' : cliente['Endereço'], 'Telefone': cliente['Telefone'] }
  print('Cliente registrado com sucesso')
  sleep(2)
  escrever_clientes_arquivo(clientes_registrados)
  os.system('cls')

# Função para editar dados do cliente
def editar_dados(listagem_clientes, clientes_registrados): 
  print('Insira o código e o nome do cliente que você deseja editar')
  edicao = int(input('Código: '))
  if clientes_registrados.get(edicao) == None:
    print('Código inexistente')
    sleep(2)
  else:
    print('Atualização do cadastro :')
    cliente = dados_cliente()
    clientes_registrados[edicao] = cliente
    print('Cliente atualizado com sucesso')
    escrever_clientes_arquivo(clientes_registrados)
    sleep(2)
  os.system('cls')
  #listagem_clientes[cliente['Nome']] = {'Endereço' : cliente['Endereço'], 'Telefone': cliente['Telefone'] } 
 

# Função para excluir dados do cliente
def excluir_cliente(listagem_clientes, clientes_registrados):  
  print('Insira o código e nome do cliente que você deseja excluir')   
  edicao = int(input('Código: '))
  if clientes_registrados.get(edicao) == None:
    print('Código inexistente')
    sleep(2)
  else:
    clientes_registrados.pop(edicao)
    print('Cliente excluido com sucesso')
    escrever_clientes_arquivo(clientes_registrados)
    sleep(2)
  os.system('cls')
  #listagem_clientes.pop(nome)
  
  
# Função para registrar uma nova manutenção
def nova_manutencao(manutencoes_agendadas):
  manutencao = dados_manutencao()
  manutencoes_agendadas[codigo_da_manutencao] = manutencao
  print('Manutenção criada com sucesso')   
 # with open('lista.txt', 'r+') as arquivo:
  #    arquivo.write(f'{codigo_da_manutencao}{manutencoes_agendadas[codigo_da_manutencao]}\n')

def editar_manutencao(manutencoes_agendadas):
  print('Insira o código da manutenção que você deseja editar')
  edicao = int(input('Código: '))
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
  else:
    manutencao = dados_manutencao()
    manutencoes_agendadas[edicao] = manutencao
    print('Manutenção editada com sucesso')


def excluir_manutencao(manutencoes_agendadas): 
  print('Insira o código da manutenção que você deseja excluir')   
  edicao = int(input('Código: '))
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
  else:
    manutencoes_agendadas.pop(edicao)
    print('Manutenção excluida com sucesso')


def realizar_manutencao(manutencoes_agendadas, manutencoes_realizadas):
  print('Insira o código da manutenção que você deseja realizar')   
  edicao = int(input('Código: '))
  if manutencoes_agendadas.get(edicao) == None:
    print('Código inexistente')
  else:
    manutencoes_realizadas[edicao] = manutencoes_agendadas[edicao]
    manutencoes_agendadas.pop(edicao)
    print('Manutenção realizada com sucesso')
    return edicao
    


#def imprimir_manutencoes(manutencoes_agendadas):
 # with open('lista.txt', 'r+') as arquivo:
  #  for elemento in manutencoes_agendadas:
   #   arquivo.write(f'{elemento}{manutencoes_agendadas[elemento]}\n')
   # for linha in arquivo:
    #  print(linha)
  #return arquivo

# ______________________nota: OS NOMES IGUAIS DAO ERRO NA LISTAGEM_________________________________-

# Programa Principal
resposta = menu()
while resposta != '0':
  
  # Novo cliente
  if resposta == '1':
   novo_cliente(listagem_clientes, clientes_registrados, codigo_do_cliente)
   codigo_do_cliente += 1
   resposta = menu()
  
  # Editar cliente 
  elif resposta == '2':  
    tabela(clientes_registrados)
    edicao = editar_dados(listagem_clientes, clientes_registrados)
    resposta = menu()
   
  # Excluir cliente
  elif resposta == '3':
    tabela(clientes_registrados)
    excluir_cliente(listagem_clientes, clientes_registrados)
    resposta = menu()

  # Listar clientes
  elif resposta == '4':
    print('Digite:')
    print('(U) Listar apenas um cliente') 
    print('(T) Para listar todos os clientes ')
    pergunta = input(' ').upper()
    if pergunta == 'T': 
      print('Lista de Clientes :')
      print('')
      tabela(clientes_registrados)
      resposta = menu()
      

    
    elif pergunta == 'U': 
      ver = int(input('Digite o código do cliente que deseja ver '))
      exibir = clientes_registrados.get(ver)
      if exibir == None:
        print('Código inexistente')
      else:
        print(ver, exibir)
      resposta = menu()
    
  
  # Nova manutenção
  elif resposta == '5':
    nova_manutencao(manutencoes_agendadas)
    codigo_da_manutencao += 1
    resposta = menu()
  
  # Editar manutenção
  elif resposta == '6':
    editar_manutencao(manutencoes_agendadas)
    resposta = menu()
    
  # Excluir manutenção
  elif resposta == '7':
    excluir_manutencao(manutencoes_agendadas)
    resposta = menu()
  
  # Realizar manutenção
  elif resposta == '8':
    edicao = realizar_manutencao(manutencoes_agendadas, manutencoes_realizadas)
    pergunta = input('Deseja marcar uma nova manutenção (s) ou (n) ?').upper()
    if pergunta == 'S':
      pergunta2 = input('Deseja marcar automaticamente ou manualmente? (a) ou (m) ?').upper()
      if pergunta2 == 'M':
        manutencao = {}
        manutencao['Custo da peça'] = input('Custo da peça ')
        manutencao['Nome da peça'] = input('Nome da peça ')
        manutencao['Prazo de validade'] = input('Prazo de validade ')
        manutencao['Cliente'] = edicao
        manutencoes_agendadas[codigo_da_manutencao] = manutencao
      elif pergunta2 == 'A':
        manutencoes_agendadas[codigo_da_manutencao] = manutencoes_realizadas[edicao]

    resposta = menu()

  # Listar manutenções
  elif resposta == '9':
    print('AGENDADAS:')
    print(manutencoes_agendadas)
    print('REALIZADAS:')
    print(manutencoes_realizadas)
    resposta = menu()

  elif resposta == '10':
    #arquivo = imprimir_manutencoes(manutencoes_agendadas)

    resposta = menu()
    

if resposta == '0':
  print('Fim do Registro')
  sleep(3)








#from datetime import date

#data_atual = date.today()
#print(data_atual)
