def agenda():
  print('''
  ░█████╗░░██████╗░███████╗███╗░░██╗██████╗░░█████╗░
  ██╔══██╗██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗
  ███████║██║░░██╗░█████╗░░██╔██╗██║██║░░██║███████║
  ██╔══██║██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║
  ██║░░██║╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║
  ╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝
  ''')

def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {'nome': nome_contato, 'telefone': telefone_contato, 'e-mail': email_contato, 'favorito': False}
  contatos.append(contato)    

def visualizar_contato(contatos):
  for indice, contato in enumerate(contatos, start=1):
    nome_contato = contato['nome']
    status = '☆' if contato['favorito'] else ' '
    print(f'{indice}. [{status}] {nome_contato}')

def editar_contato(contados, indice_contato, novo_nome_contato):
  indice_contato_ajustado = int(indice_contato)-1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado <= len(contatos):
    contados[indice_contato_ajustado]['nome'] = novo_nome_contato
    print(f'Tarefa {indice_contato_ajustado} atualizada para {novo_nome_contato}')
  else:
    print('Índice do contato inválido.')  
  return

def marcar_favorito(contados, indice_contato):
  indice_contato_ajustado = int(indice_contato)-1
  contatos[indice_contato_ajustado]['favorito'] = not contatos[indice_contato_ajustado]['favorito']
  mensagem = 'marcado' if contatos[indice_contato_ajustado]['favorito'] else 'Desmarcado'
  print(mensagem)
  return

def visualizar_favorito(contatos):
  for indice, contato in enumerate(contatos, start=1):
    nome_contato = contato['nome']
    if contato['favorito']:
      print(print(f'{indice} - {nome_contato}'))
  return  

def excluir_contato(contatos, indice_contato):
  for indice, contato in enumerate(contatos, start=1):
    if indice == int(indice_contato):
      contatos.remove(contato)  
  return

contatos = []

while True:
  agenda()
  print('1 - Adicionar contato')
  print('2 - Visualizar contato')
  print('3 - Editar contato')
  print('4 - Marcar/Desmarcar contato como favorito')
  print('5 - Visualizar contato marcado como favorito ')
  print('6 - Excluir contato')
  print('7 - Sair do programa')

  opcao = input('Esolha um opção: ')

  if opcao == '1':
    nome_contato = input('Informe o nome do contato: ')
    telefone_contato = input('Infome o telefone do contato: ')
    email_contato = input('Informe o e-mail do contato: ')
    adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
  elif opcao == '2':
    visualizar_contato(contatos) 
  elif opcao == '3':
    indice_contato = input('Informe o índice do contato: ')
    novo_nome = input('Informe um novo nome de contato: ')
    editar_contato(contatos, indice_contato, novo_nome)
  elif opcao == '4':
    indice_contato = input('Informe o índice do contato: ')
    marcar_favorito(contatos, indice_contato)
  elif opcao == '5':
    visualizar_favorito(contatos)
  elif opcao == '6':
    indice = input('Informe o índice do contato que deseja excluir: ')
    excluir_contato(contatos, indice)    
  elif opcao == '7':
    break
print('programa finalizado')  