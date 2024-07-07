
import os


#criação de Lista
#restaurantes = ['Pizza','Sushi']

#dicionario
restaurantes = [{'nome':'Pizaria ABC','categoria':'Italiana','ativo':False},
                {'nome':'Sushi','categoria':'Japonesa','ativo':True},
                {'nome':'Hamburgueria','categoria':'Pizza','ativo':True}
]


def exibir_nome_programa():
    ''' Exibe o nome do programa na tela
    '''
    print('𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤')

def exibir_opcoes():
## print 
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Alter estado do Restaurantes')
    print('4. Sair\n')

# criando função def 

def finalizar_app():
    exibir_subtitulo('Finalizando App')

def opcao_invalida():
    print('Opção inválida!')
    main()

def voltar_menu():
    input('\nDigite uma tecla para voltar o meu principal: ')
    main()

## como essa função de exibir subtitulo estava sendo usada em diversas partes do caodigo foi criada uma função
def exibir_subtitulo(texto):
     '''Limpa tela  e exibe o titulo com *'''
     os.system('cls')
     linha = '*'  * (len(texto) + 4)
     print(linha)
     print(texto)
     print(linha)

def cadastrar_novo_restaurente():
    '''Essa função de cadastrar um novo restaurante
    Inputs:
    -Nome do restaurante 
    -Categoria

    Outputs:
    -Adciona a lista um novo restaurante
    '''
    exibir_subtitulo('Cadastros de Novos restaurantes\n')

    nome_restaurente = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurente} : ')

    dados_do_restaurante = {'nome':nome_restaurente,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'Restaurente {nome_restaurente} foi cadastrado com sucesso! \n')
    voltar_menu()

def listando_restaurantes():
    '''Essa função de Lista todos restaurantes
    Inputs:

    Outputs:
    -Lista de restaurantes cadastrados
    '''

    exibir_subtitulo('Listando Restaurantes:\n')
    
    print(f'{'Nome Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Estado'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_menu()

def alternar_estado_restaurante():
     '''Essa função de alterar o estado de um restaurante
     
     Inputs:
     - Nome do restaurantes que deseja alterar o estado

     Output:
     - Novo estado do restaurante
     '''
     exibir_subtitulo('Alternando o estado do restaurante:\n')

     nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
     restaurante_encontrado = False
     for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mesagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mesagem)
     if not restaurante_encontrado:
        print('o restaurante não foi encontrado')
     voltar_menu()

def escolher_opcao():
    '''Essa função de Escolha do menu
    
    Inputs:
    - Opção de escolha em valor(Int)

    '''
# try -except para não "quebrar o code quando digita algo fora do padrão"
    try:
        ## input 
        opção_escolha = int(input('Escolha uma opção: '))

## Match é uma alternativa pro if esle elif

        match opção_escolha:
            case 1:
                cadastrar_novo_restaurente()
            case 2:
                listando_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                print('Finalizar app')
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


# ## if else

#     if opção_escolha == 1:
#         print('1. Cadastrar Restaurantes')
#     elif opção_escolha == 2:
#         print('2. Listar Restaurantes')
#     elif opção_escolha == 3:
#         print('3. Ativar Restaurantes')
#     else:
#         finalizar_app()


## deixando o programa como Main

def main():
    '''Função Main do programa essa é a função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()