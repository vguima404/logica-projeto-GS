# Lista com bairros e seus respectivos níveis de risco de enchente
zonas = [
    {"bairro": "Centro", "risco": "alto"},
    {"bairro": "Quitandinha", "risco": "baixo"},
    {"bairro": "Itaipava", "risco": "alto"},
    {"bairro": "Alto da Serra", "risco": "alto"},
    {"bairro": "Corrêas", "risco": "moderado"},
]

# Lista com abrigos disponíveis, contendo nome, endereço e capacidade
abrigos = [
    {"nome": "Pátio Petrópolis Shopping", "endereco": "Rua Marechal Deodoro, 153, Centro", "capacidade": 5000},
    {"nome": "Escola Municipal Vereador José Fernandes da Silva", "endereco": "Rua Teresa, 1781, Alto da Serra", "capacidade": 300},
    {"nome": "CIEP 472 Candido Portinari", "endereco": "Estr. União e Indústria, 11960, Itaipava", "capacidade": 1000},
    {"nome": "CPTI/FAETERJ", "endereco": "Av. Getulio Vargas, 335, Quitandinha", "capacidade": 400},
    {"nome": "Academia Master", "endereco": "R. José Cândido, 143 - Corrêas", "capacidade": 50},
]

# Dicionário com rotas seguras cadastradas por bairro
rotas_seguras_por_bairro = {
    "Centro": [
        "Rua Marechal Deodoro (acesso direto ao shopping)",
        "Rua do Imperador",
        "Rua Floriano Peixoto",
        "Rua General Osório"
    ],
    "Alto da Serra": [
        "Rua Teresa (acesso direto à escola)",
        "Rua Henrique Dias",
        "Rua Bernardo de Vasconcelos",
        "Rua Luiz Winter"
    ],
    "Itaipava": [
        "Estrada União e Indústria",
        "Rua Joaquim Agante Moço",
        "Avenida Leopoldina",
        "Rua Professor Veiga"
    ],
    "Quitandinha": [
        "Avenida Getúlio Vargas",
        "Rua General Rondon",
        "Rua Cândido Portinari"
    ],
    "Corrêas": [
        "Rua Vigário Corrêa",
        "Rua Manuel Torres",
        "Rua Lopes Trovão"
    ]
}

# Função que exibe todos os bairros e seus respectivos níveis de risco
def exibir_zonas_de_risco():
    print("\n Zonas de Risco de Enchente:")
    for zona in zonas:
        print(f"- Bairro: {zona['bairro']} | Nível de risco: {zona['risco'].capitalize()}")

# Função que gera um alerta com base no bairro informado
def gerar_alerta(bairro):
    bairro_formatado = bairro.strip().lower()  # Remove espaços e converte para minúsculas
    zona_encontrada = False

    for zona in zonas:
        if zona['bairro'].lower() == bairro_formatado:
            zona_encontrada = True
            risco = zona['risco']

            # Exibe alerta específico dependendo do nível de risco
            if risco == "alto":
                print("ALERTA: Risco ALTO de enchente na sua área!")

                # Usa match-case para selecionar o bairro e recomendar abrigo e rota
                match bairro_formatado:
                    case "centro":
                        print(f"Se abrigue no local mais próximo de você! {abrigos[0]}")
                        print(f"Siga por uma dessas rotas para chegar até lá: {rotas_seguras_por_bairro['Centro']}")
                        break

                    case "alto da serra":
                        print(f"Se abrigue no local mais próximo de você! {abrigos[1]}")
                        print(f"Siga por uma dessas rotas para chegar até lá: {rotas_seguras_por_bairro['Alto da Serra']}")
                        break

                    case "itaipava":
                        print(f"Se abrigue no local mais próximo de você! {abrigos[2]}")
                        print(f"Siga por uma dessas rotas para chegar até lá: {rotas_seguras_por_bairro['Itaipava']}")
                        break

            elif risco == "moderado":
                print("Atenção: Risco MODERADO de alagamento.")
            else:
                print("Sua área está SEGURA no momento!")

    # Caso o bairro informado não esteja na lista
    if not zona_encontrada:
        print('Bairro não encontrado!')

# Função que mostra as rotas seguras de um bairro específico
def buscar_rotas_seguras(bairro):
    bairro.lower()
    print(f"\n Rotas seguras para o bairro: {bairro.capitalize()}")
    rotas = rotas_seguras_por_bairro.get(bairro.capitalize(), [])  # Tenta buscar rotas para o bairro, se não encontrar, retorna uma lista vazia como padrão

    if rotas:
        for rota in rotas:
            print(f"-> {rota}")
    else:
        print("Nenhuma segura foi cadastrada para esse bairro.")

# Função que exibe os abrigos localizados no bairro informado
def exibir_abrigos(bairro):
    encontrou = False  # Variável de controle para saber se encontrou abrigo

    print(f"Abrigos disponíveis no bairro {bairro}:")

    for abrigo in abrigos:
        # Verifica se o nome do bairro está presente no endereço do abrigo
        if bairro.lower() in abrigo['endereco'].lower():
            print(f"- {abrigo['nome']} | Endereço: {abrigo['endereco']} | Capacidade: {abrigo['capacidade']}")
            encontrou = True

    if not encontrou:
        print(f"Nenhum abrigo encontrado nesse bairro!")

# Função principal que mostra um menu de opções ao usuário
def menu():
    while True:
        # Exibe o menu de opções
        print("1 - Exibir bairros e seus respectivos graus de risco")
        print("2 - Visualizar se seu bairro está em estado de alerta")
        print("3 - Buscar rotas seguras")
        print("4 - Exibir abrigos")
        print("5 - Sair")

        # Recebe a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Executa a função correspondente à opção escolhida
        match opcao:
            case "1":
                exibir_zonas_de_risco()

            case "2":
                gerar_alerta(input("Digite o bairro que deseja visualizar: "))

            case "3":
                buscar_rotas_seguras(input("Digite o bairro que deseja ir: "))

            case "4":
                exibir_abrigos(input("Digite o bairro que deseja visualizar o abrigo: "))

            case "5":
                print("Saindo...")
                break  # Encerra o loop e finaliza o programa

# Chamada da função principal para iniciar o programa
menu()