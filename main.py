zonas = [
    {"bairro": "Centro", "risco": "alto"},
    {"bairro": "Quitandinha", "risco": "baixo"},
    {"bairro": "Itaipava", "risco": "alto"},
    {"bairro": "Alto da Serra", "risco": "alto"},
    {"bairro": "Corrêas", "risco": "moderado"},
]

abrigos = [
    {"nome": "Pátio Petrópolis Shopping", "endereco": "Rua Marechal Deodoro, 153, Centro", "capacidade": 5000},
    {"nome": "Escola Municipal Vereador José Fernandes da Silva", "endereco": "Rua Teresa, 1781, Alto da Serra", "capacidade": 300},
    {"nome": "CIEP 472 Candido Portinari", "endereco": "Estr. União e Indústria, 11960, Itaipava", "capacidade": 1000},
    {"nome": "CPTI/FAETERJ", "endereco": "Av. Getulio Vargas, 335, Quitandinha", "capacidade": 400},
    {"nome": "Academia Master", "endereco": "R. José Cândido, 143 - Corrêas", "capacidade": 50},
]

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



def exibir_zonas_de_risco():
    print("\n Zonas de Risco de Enchente:")
    for zona in zonas:
        print(f"- Bairro: {zona['bairro']} | Nível de risco: {zona['risco'].capitalize()}")


def gerar_alerta(bairro):

    bairro_formatado = bairro.strip().lower()
    zona_encontrada = False

    for zona in zonas:

        if zona['bairro'].lower() == bairro_formatado:
            zona_encontrada = True
            risco = zona['risco']

            if risco == "alto":
                print ("ALERTA: Risco ALTO de enchente na sua área!")

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


    if not zona_encontrada:
        print('Bairro não encontrado!')


def buscar_rotas_seguras(bairro):
    print(f"\n Rotas seguras para o bairro: {bairro}")

    rotas = rotas_seguras_por_bairro.get(bairro, [])
    if rotas:
        for rota in rotas:
            print(f"-> {rota}")
    else:
        print("Nenhuma segura foi cadastrada para esse bairro.")

