# FIAP GLOBAL SOLUTION - COMPUTIIONAL THINKING WITH PYTHON
# ENGEHARIA DE SOFTWARE - 1º ANO (NOTURNO)
# ALUNOS:
# ALEXANDRE ASSIS DO NASCIMENTO - RM: 558927
# HERBERT DE SOUZA - RM: 555701

# garantindo que o usuário não digite uma letra
def checar_letra(opcao):
    while not opcao.isnumeric():
        print('ATENÇÃO: Letras NÃO são permitidas. Digite um dos números correspondentes!!')
        opcao = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
    opcao = int(opcao)
    return opcao

# garantindo que o usuário digite somente 1, 2 ou 3
def checar_num(opcao):
    while opcao > 3:
        print('ATENÇÃO: Digite 1, 2, ou 3!!')
        opcao = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
        opcao = checar_letra(opcao)
    opcao = int(opcao)
    return opcao

# exibindo menu de cadastro dos resíduos
def cadastrar_residuos(residuo):
    residuo = input(
        '==============\nTABELA DE RESÍDUOS\n==============\nPAPEL: 10 pontos/kg\nMETAL: 20 pontos/kg\nVIDRO: 20 pontos/kg\nPLASTICO: 50 pontos/kg\nCadastre o seu resíduo (Insira o nome corretamente do resíduo que quer cadastrar, 1 por vez).\n-> ')
    sim_ou_nao = input('Deseja adicionar mais resíduos os carrinho?\nDigite S/s ou N/n\n-> ')
    return residuo, sim_ou_nao

# exibindo menu principal, para usar em diferentes partes do código
def exibir_menu(menu):
    menu = input('===============\nSEASCASH MENU\n===============\n1- Cadastro de Resíduos\n2- Verificar SALDO de pontos\n-> ')
    menu = checar_letra(menu)
    menu = checar_num(menu)
    menu = int(menu)
    return menu

print('============================')
print('Bem vindo(a) ao SEASCASH - O CashBack dos Mares!\nAqui você vai conseguir descartar seus resíduos e trocar eles por pontos e ganhar recompensas exclusivas e até desconto no IPTU!')
print('============================')
print()

# criando lista de usuários com usuário padrão
lista_usuarios = ['user1']

# exibindo menu inicial
escolha_usuario = input('Digite 1 para fazer LOGIN\nDigite 2 para se CADASTRAR\nDigite 3 para encerrar\n -> ')
# obrigando resposta do usuário ser apenas 1, 2 e 3
escolha_usuario = checar_letra(escolha_usuario)
escolha_usuario = checar_num(escolha_usuario)

# iniciando o loop para o SEASCASH ficar rodando
while True:
    # iniciando o loop das opções de fazer login e criar usuário
    while escolha_usuario != 3:
        # realizando login no SEASCASH
        if escolha_usuario == 1:
            username = input('Digite seu username para fazer login: ')
            if username in lista_usuarios:
                print('LOGADO(A) com sucesso!! :)')

                # iniciando menu principal do SEASCASH
                opcao_menu = ''
                opcao_menu = exibir_menu(opcao_menu)

                # iniciando loop para cadastrar os resíduos
                while opcao_menu == 1:
                    lista_residuos = []
                    lista_pontos = []
                    lista_kilos = []

                    # iniciando cadastro dos resíduos
                    residuo = ''
                    kilo = int(input(f'Quantos kilos você vai descartar desse resíduo? -> '))
                    lista_kilos.append(kilo)
                    residuo, sim_ou_nao = cadastrar_residuos(residuo)
                    lista_residuos.append(residuo)

                    # perguntando ao usuário se ele quer cadastrar mais resíduos
                    while sim_ou_nao == 'S' or sim_ou_nao == 's':
                        kilo = int(input(f'Quantos kilos você vai descartar? -> '))
                        lista_kilos.append(kilo)
                        residuo, sim_ou_nao = cadastrar_residuos(residuo)
                        lista_residuos.append(residuo)
                    break
                # voltando ao menu principal caso o usuário responda não
                opcao_menu = exibir_menu(opcao_menu)

                # verificando pontuação total do usuário
                if opcao_menu == 2:
                    # determinando a quantidade de pontos de cada resíduo e multiplicando pelo kilo, seguindo a ordem do índice
                    for i in range(len(lista_residuos)):
                        residuo_indice = lista_residuos[i]
                        kilo = lista_kilos[i]
                        if residuo_indice == 'Papel' or residuo_indice == 'papel':
                            lista_pontos.append(10 * kilo)
                        elif residuo_indice == 'Metal' or residuo_indice == 'metal':
                            lista_pontos.append(20 * kilo)
                        elif residuo_indice == 'Vidro' or residuo_indice == 'vidro':
                            lista_pontos.append(20 * kilo)
                        elif residuo_indice == 'Plastico' or residuo_indice == 'plastico':
                            lista_pontos.append(50 * kilo)
                    # somando os pontos totais e exibindo ao usuário
                    total_pontos = 0
                    for pontos in lista_pontos:
                        total_pontos += pontos
                    print(
                        f'Resíduos descartados: {lista_residuos}\nPARABÉNS, {username}, seu Saldo total é de: {total_pontos} pontos!\nConsulte os estabelecimentos parceiros por meio dos seus sites ou pessoalmente para se informar sobre as trocas de pontos por recompensas exclusivas\nAo atingir 250 pontos, você pode utilizar seus pontos para ganhar 10% de desconto no IPTU\nAo atingir 500 pontos, você pode utilizar seus pontos para ganhar 30% de desconto no IPTU\nAo atingir 1000 pontos, você pode utilizar seus pontospara ganhar 80% de desconto no IPTU')
                    print(
                        'Agradecemos pela participação no projeto. Graças a você esses resíduos evitaram de irem parar no o OCEANO!\n')
                    print('O programa foi encerrado.')
                    break
            # dando opção ao usuário de criar um nome de usuário, caso ele tente fazer login com nome de usuário inexistente
            else:
                escolha_usuario = input(
                    'Não foi encontrado um usuário com esse nome na nossa base de dados.\nDigite 2 para fazer seu cadastro.\n-> ')
                escolha_usuario = int(escolha_usuario)
        # iniciando cadastro de novo usuário no SEASCASH
        if escolha_usuario == 2:
            cadastro_user = input('Faça seu cadastro no SEASCASH. Digite um username: ')
            while cadastro_user in lista_usuarios:
                cadastro_user = input('O nome de usuário digitado JÁ EXISTE. Digite outro\n-> ')
            lista_usuarios.append(cadastro_user)
            print(f'Cadastro realizado com sucesso!!!\nFaça login para acessar a plataforma do SEASCASH.')
        # garantindo que após o cadastro, o usuário seja levado ao menu principal
        escolha_usuario = 1
    print('O programa será encerrado agora.')
    break




