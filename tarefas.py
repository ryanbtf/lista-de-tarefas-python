import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []
    
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefas(tarefas):
    titulo = input("Digite a tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("\nTarefa adicionada!\n")

def listar_tarefas(tarefas):
    print("-"*40)
    print("# LISTA DE TAREFAS #")
    for i, t in enumerate(tarefas):
        status = "✔" if t["concluida"] else "✘"
        print(f"\n{i} - {t['titulo']} [{status}]\n")
    print("-"*40)

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    i = int(input("Qual tarefa concluir?: "))
    tarefas[i]["concluida"] = True
    print("\nTarefa concluída!\n")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    i = int(input("Qual tarefa remover?: "))
    tarefas.pop(i)

def menu():
    tarefas = carregar_tarefas()

    while True:

        print("-"*40)
        print("Gerenciador de Tarefas")
        print("-"*40)
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefas(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            salvar_tarefas(tarefas)
            break
        else:
            print("\nOpção inválida!\n")
        
menu()
