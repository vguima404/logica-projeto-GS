zonas = [
    {"bairro": "Centro", "risco": "alto"},
    {"bairro": "Quitandinha", "risco": "moderado"},
    {"bairro": "Itaipava", "risco": "baixo"},
    {"bairro": "Alto da Serra", "risco": "alto"},
    {"bairro": "Corrêas", "risco": "moderado"},
]

abrigos = [
    {"nome": "Pátio Petrópolis Shopping", "endereco": "Rua Marechal Deodoro, 153, Centro", "capacidade": 5000},
    {"nome": "Escola Municipal Vereador José Fernandes da Silva", "endereco": "Rua Teresa, 1781, Alto da Serra", "capacidade": 300},
    {"nome": "CIEP 472 Candido Portinari", "endereco": "Estr. União e Indústria, 11960, Itaipava", "capacidade": 1000},
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
    ]
}



def exibir_zonas_de_risco():
    print("\n Zonas de Risco de Enchente:")
    for zona in zonas:
        print(f"- Bairro: {zona['bairro']} | Nível de risco: {zona['risco'].capitalize()}")

