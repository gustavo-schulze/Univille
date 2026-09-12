#Programa de enquete com votação

import os


# Cadastra uma nova opção de voto no dicionário (nome -> quantidade de votos)
def cadastrar_opcao(opcoes):
    nome = input("Digite o nome da nova opção: ").strip()
    if not nome:
        print("Nome inválido. A opção não pode ser vazia.\n")
        return
    if nome in opcoes:
        print("Essa opção já existe.\n")
        return
    opcoes[nome] = 0
    print(f"Opção '{nome}' cadastrada com sucesso!\n")


# Exibe as opções cadastradas, numeradas
def listar_opcoes(opcoes):
    if not opcoes:
        print("Nenhuma opção cadastrada ainda.\n")
        return
    print("Opções cadastradas:")
    for i, nome in enumerate(opcoes, start=1):
        print(f"{i}. {nome}")
    print()


# Incrementa o contador de votos da opção escolhida pelo participante
def registrar_voto(opcoes):
    if not opcoes:
        print("Nenhuma opção cadastrada para votar.\n")
        return

    listar_opcoes(opcoes)
    nomes = list(opcoes.keys())
    escolha = input("Digite o número da opção em que deseja votar: ").strip()

    if not escolha.isdigit() or not (1 <= int(escolha) <= len(nomes)):
        print("Opção não encontrada.\n")
        return

    nome_escolhido = nomes[int(escolha) - 1]
    opcoes[nome_escolhido] += 1
    print(f"Voto registrado em '{nome_escolhido}'!\n")


# Mostra a quantidade bruta de votos de cada opção
def consultar_votos(opcoes):
    if not opcoes:
        print("Nenhuma opção cadastrada ainda.\n")
        return
    print("Quantidade de votos:")
    for nome, votos in opcoes.items():
        print(f"{nome}: {votos} voto(s)")
    print()


# Mostra quantidade e percentual de votos de cada opção em relação ao total
def mostrar_resultado(opcoes):
    if not opcoes:
        print("Nenhuma opção cadastrada ainda.\n")
        return

    total_votos = sum(opcoes.values())
    print("Resultado da enquete:")
    for nome, votos in opcoes.items():
        percentual = (votos / total_votos * 100) if total_votos > 0 else 0
        print(f"{nome}: {votos} voto(s) - {percentual:.2f}%")
    print()


# Determina a opção (ou opções, em caso de empate) com mais votos
def mostrar_vencedora(opcoes):
    if not opcoes:
        print("Nenhuma opção cadastrada ainda.\n")
        return

    maior_votos = max(opcoes.values())

    if maior_votos == 0:
        print("Ainda não há votos registrados.\n")
        return

    vencedoras = [nome for nome, votos in opcoes.items() if votos == maior_votos]

    if len(vencedoras) == 1:
        print(f"A opção vencedora é '{vencedoras[0]}' com {maior_votos} voto(s)!\n")
    else:
        empate = ", ".join(vencedoras)
        print(f"Houve um empate entre as opções: {empate} (cada uma com {maior_votos} voto(s)).\n")


# Imprime as opções do menu principal
def exibir_menu():
    print("===== MENU DA ENQUETE =====")
    print("1. Cadastrar opção")
    print("2. Listar opções")
    print("3. Registrar voto")
    print("4. Consultar quantidade de votos")
    print("5. Mostrar resultado")
    print("6. Mostrar opção vencedora")
    print("7. Encerrar")


# Loop principal: exibe o menu e direciona para a função correspondente
def main():
    opcoes = {}  # dicionário nome_da_opcao -> quantidade de votos

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        print()

        if escolha == "1":
            cadastrar_opcao(opcoes)
        elif escolha == "2":
            listar_opcoes(opcoes)
        elif escolha == "3":
            registrar_voto(opcoes)
        elif escolha == "4":
            consultar_votos(opcoes)
        elif escolha == "5":
            mostrar_resultado(opcoes)
        elif escolha == "6":
            mostrar_vencedora(opcoes)
        elif escolha == "7":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
