import os
import csv
import random

arquivo_receitas = "receitas.csv"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpar_tela()
        print("""
██████╗ ███████╗██████╗ ███████╗██╗████████╗ █████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔════╝██║╚══██╔══╝██╔══██╗██╔════╝
██████╔╝█████╗  ██║     █████╗  ██║   ██║   ███████║███████╗
██╔══██╗██╔══╝  ██║     ██╔══╝  ██║   ██║   ██╔══██║╚════██║
██║  ██║███████╗╚██████╗███████╗██║   ██║   ██║  ██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
            """)
        print("1 - Adicionar Nova Receita")
        print("2 - Visualizar Todas as Receitas")
        print("3 - Visualizar Receitas Favoritas")
        print("4 - Atualizar Receita Existente")
        print("5 - Deletar Receita")
        print("6 - Adicionar Receita aos Favoritos")
        print("7 - Filtrar Receitas Por País")
        print("8 - Sugestão de Receita Aleatória")
        print("9 - Escolher receita por ingredientes")
        
        
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_receita()
        elif escolha == '2':
            visualizar_receitas()
        elif escolha == '3':
            visualizar_fav()
        elif escolha == '4':
            atualizar_receita()
        elif escolha == '5':
            deletar_receita()
        elif escolha == '6':
            fav()
        elif escolha == '7':
            filtrar_por_pais()
        elif escolha == '8':
            receita_aleatoria()
        elif escolha == '9':
            buscar_por_ingredientes()
        elif escolha == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")
        
        input("Pressione Enter para continuar...")

def adicionar_receita():
    nome = input("Nome da receita: ")
    pais = input("País de origem: ")
    ingredientes = input("Ingredientes (separados por vírgula): ")
    modo_preparo = input("Modo de preparo: ")
    nova_receita = [nome, pais, ingredientes, modo_preparo, "False"]
    
    try:
        with open(arquivo_receitas, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(nova_receita)
        
        print("Receita adicionada com sucesso!\n")
    except Exception:
        print("Erro ao adicionar receita!\n")

def visualizar_receitas():
    try:
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, 1):
                print(f"{i}. Nome: {row[0]}, País: {row[1]}, Ingredientes: {row[2]}, Modo de Preparo: {row[3]}, Favorito: {row[4]}")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

def visualizar_fav():
    try:
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            favoritos = [row for row in reader if row[4].lower() == "true"] #list comprehension para reduzir linhas do codigo
            if favoritos:
                for i, row in enumerate(favoritos, 1):
                    print(f"{i}. Nome: {row[0]}, País: {row[1]}, Ingredientes: {row[2]}, Modo de Preparo: {row[3]}, Favorito: {row[4]}")
            else:
                print("Não há receitas favoritas.\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")

def atualizar_receita():
    visualizar_receitas()
    try:
        index = int(input("Digite o número da receita que deseja atualizar: ")) - 1
        receitas = []
        
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            receitas = list(reader)
        
        if 0 <= index < len(receitas):
            nome = input("Novo nome da receita (deixe em branco para não alterar): ")
            pais = input("Novo país de origem (deixe em branco para não alterar): ")
            ingredientes = input("Novos ingredientes (deixe em branco para não alterar): ")
            modo_preparo = input("Novo modo de preparo (deixe em branco para não alterar): ")
            
            if nome:
                receitas[index][0] = nome
            if pais:
                receitas[index][1] = pais
            if ingredientes:
                receitas[index][2] = ingredientes
            if modo_preparo:
                receitas[index][3] = modo_preparo
            
            with open(arquivo_receitas, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(receitas)
        
        print("Receita atualizada com sucesso!\n")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.\n")
    else:
        print("Número da receita inválido.\n")

def deletar_receita():
    visualizar_receitas()
    try:
        index = int(input("Digite o número da receita que deseja deletar: ")) - 1
        receitas = []
        
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            receitas = list(reader)
        
        if 0 <= index < len(receitas):
            receitas.pop(index)
            
            with open(arquivo_receitas, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(receitas)
            
            print("Receita deletada com sucesso!\n")
        else:
            print("Número da receita inválido.\n")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.\n")

def filtrar_por_pais():
    pais_desejado = input("Digite o país cujas receitas você deseja visualizar: ").lower()
    encontrou = False
    
    try:
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1].lower() == pais_desejado:
                    print(f"Nome: {row[0]}, Ingredientes: {row[2]}, Modo de Preparo: {row[3]}, Favorito: {row[4]}")
                    encontrou = True
        
        if not encontrou:
            print("Não foram encontradas receitas para o país informado.\n")
    except FileNotFoundError:
        print("Ainda não há nenhuma receita cadastrada!\n")
    except Exception:
        print("Ocorreu um erro ao ler as receitas!\n")

def receita_aleatoria():
    try:
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            receitas = list(reader)
            receita_aleatoria = random.choice(receitas)
            print("Sugestão de receita aleatória: ")
            print(f'Nome: {receita_aleatoria[0]}')
            print(f'País: {receita_aleatoria[1]}')
            print(f'Ingredientes: {receita_aleatoria[2]}')
            print(f'Modo de preparo: {receita_aleatoria[3]}')
            print(f'Favorito: {receita_aleatoria[4]}')
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")
    except Exception:
        print("Erro ao adicionar uma receita aleatória!\n")

def buscar_por_ingredientes():
    ingredientes_desejados = set(input("Digite os ingredientes desejados (separados por vírgula): ").split(", "))
    encontrou = False 
    
    with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            ingredientes_receita = set(row[2].split(", "))
            if ingredientes_desejados.issubset(ingredientes_receita):
                print(f"Nome: {row[0]}, País: {row[1]}, Modo de Preparo: {row[3]}, Favorito: {row[4]}")
                encontrou = True
    
    if not encontrou:
        print("Não foram encontradas receitas com os ingredientes informados.\n")

def fav():
    nome_receita = input("Digite o nome da receita que deseja adicionar aos favoritos: ")
    receitas = []
    
    try:
        with open(arquivo_receitas, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            receitas = list(reader)
        
        encontrou = False
        for receita in receitas:
            if receita[0].lower() == nome_receita.lower():
                receita[4] = "True"
                encontrou = True
                break
        
        if encontrou:
            with open(arquivo_receitas, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(receitas)
            print("Receita adicionada aos favoritos com sucesso!\n")
        else:
            print("Receita não encontrada.\n")
    except FileNotFoundError:
        print("Ainda não há receitas cadastradas.\n")
    except Exception:
        print("Erro ao adicionar receita aos favoritos!\n")

if __name__ == "__main__":
    menu_principal()
