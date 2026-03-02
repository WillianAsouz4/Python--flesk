def adicionar_tarefa(tarefas, nome_tarefa):
   tarefa = {"tarefa": nome_tarefa, "completada": False}
   tarefas.append(tarefa)
   print(f"A tarefa {nome_tarefa} foi adicionada com sucesso!")
   return

def ver_tarefas(tarefas):
  print("\n Tarefas Pendentes:")
  for idx, tarefa in enumerate(tarefas, start=1):
    status = "✔" if tarefa["completada"] else " "
    print(f"{idx}. [{status}] {tarefa['tarefa']}")
    
tarefas = []


while True:
 print("\n Menu do Gerenciador de Tarefas")
 print("1. Adicionar Tarefa")
 print("2. Visualizar Tarefas")
 print("3. Atulizar Tarefa")
 print("4. Completar Tarefa")
 print("5. apagar Tafera Comculida")
 print("6. Encerar Programa")

 escolha = input("Escolha uma opção: ")
 if escolha == "1":
   # Adicionar Tarefa
   nome_tarefa = input("Digite o nome da tarefa:")
   adicionar_tarefa(tarefas, nome_tarefa)

 elif escolha == "2":
   ver_tarefas(tarefas)

   
 elif escolha == "6":
    print("Fin do Programa!")
    break